#include "collections.h"
#include "domain.h"
#include "ui.h"
#include <stdio.h>
#include <string.h>

#ifdef _WIN32
#include <windows.h>
#endif

typedef struct AppCtx {
    List playlist;
} AppCtx;

static void op_get_all(void* vctx, const List** out_list) {
    AppCtx* ctx = (AppCtx*)vctx;
    if (out_list) *out_list = &ctx->playlist;
}

static int op_add(void* vctx, const char* author, const char* title, const char* duration_str) {
    AppCtx* ctx = (AppCtx*)vctx;
    int sec = 0;
    if (!author || !title || !duration_str) return -2;
    if (track_parse_duration(duration_str, &sec) != 0) return -3;

    Track* t = track_new(author, title, sec);
    if (!t) return -4;

    if (playlist_add_track(&ctx->playlist, t) != 0) {
        track_free(t);
        return -5;
    }
    return 0;
}

static int op_remove_by_number(void* vctx, size_t one_based_index) {
    AppCtx* ctx = (AppCtx*)vctx;
    if (one_based_index == 0) return -1;
    size_t idx0 = one_based_index - 1;
    if (idx0 >= list_size(&ctx->playlist)) return -2;
    return playlist_remove_at(&ctx->playlist, idx0);
}

static void op_search_by_author(void* vctx, const char* query, List* out_results) {
    AppCtx* ctx = (AppCtx*)vctx;
    playlist_search_by_author(&ctx->playlist, query, out_results);
}

static void op_search_by_title(void* vctx, const char* query, List* out_results) {
    AppCtx* ctx = (AppCtx*)vctx;
    playlist_search_by_title(&ctx->playlist, query, out_results);
}

static void op_format_item_row(void* vctx, const void* item, long one_based_index, char* out, size_t outsz) {
    (void)vctx;
    const Track* t = (const Track*)item;
    char dur[16];
    track_format_duration(t->duration_sec, dur, sizeof(dur));
    snprintf(out, outsz, "%ld - %s - %s - %s", one_based_index, t->author, t->title, dur);
}

int main(void) {
#ifdef _WIN32
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);
#endif
    AppCtx app;
    list_init(&app.playlist);

    UiOps ops = {
        .get_all = op_get_all,
        .add = op_add,
        .remove_by_number = op_remove_by_number,
        .search_by_author = op_search_by_author,
        .search_by_title = op_search_by_title,
        .format_item_row = op_format_item_row
    };

    run_ui(&app, &ops);

    list_clear(&app.playlist, track_free);
    return 0;
}