#include "domain.h"
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdio.h>

static void safe_copy(char* dst, size_t dstsz, const char* src) {
    if (!dst || dstsz == 0) return;
    if (!src) { dst[0] = '\0'; return; }
#ifdef _MSC_VER
    strncpy_s(dst, dstsz, src, _TRUNCATE);
#else
    strncpy(dst, src, dstsz - 1);
    dst[dstsz - 1] = '\0';
#endif
}

Track* track_new(const char* author, const char* title, int duration_sec) {
    Track* t = (Track*)malloc(sizeof(Track));
    if (!t) return NULL;
    safe_copy(t->author, sizeof(t->author), author);
    safe_copy(t->title, sizeof(t->title), title);
    t->duration_sec = duration_sec >= 0 ? duration_sec : 0;
    return t;
}

void track_free(void* p) {
    if (p) free(p);
}

char* track_format_duration(int sec, char* buf, size_t bufsize) {
    if (!buf || bufsize < 1) return buf;
    if (sec < 0) sec = 0;
    int mm = sec / 60;
    int ss = sec % 60;
    snprintf(buf, bufsize, "%02d:%02d", mm, ss);
    return buf;
}

int track_parse_duration(const char* s, int* out_sec) {
    if (!s || !out_sec) return -1;
    while (isspace((unsigned char)*s)) s++;
    if (*s == '\0') return -1;

    const char* colon = strchr(s, ':');
    if (colon) {
        int mm = 0, ss = 0;
#ifdef _MSC_VER
        if (sscanf_s(s, "%d:%d", &mm, &ss) == 2 && mm >= 0 && ss >= 0 && ss < 60) {
#else
        if (sscanf(s, "%d:%d", &mm, &ss) == 2 && mm >= 0 && ss >= 0 && ss < 60) {
#endif
            * out_sec = mm * 60 + ss;
            return 0;
        }
        return -1;
        }

    char* endptr = NULL;
    long v = strtol(s, &endptr, 10);
    if (endptr == s || v < 0) return -1;
    *out_sec = (int)v;
    return 0;
    }

static int tolower_ascii(int c) { return tolower((unsigned char)c); }

static int contains_icase(const char* haystack, const char* needle) {
    if (!haystack || !needle) return 0;
    if (*needle == '\0') return 1;
    size_t nlen = strlen(needle);
    size_t hlen = strlen(haystack);
    if (nlen > hlen) return 0;

    for (size_t i = 0; i + nlen <= hlen; ++i) {
        size_t j = 0;
        while (j < nlen &&
            tolower_ascii(haystack[i + j]) == tolower_ascii(needle[j])) {
            ++j;
        }
        if (j == nlen) return 1;
    }
    return 0;
}

int playlist_add_track(List * playlist, Track * track) {
    if (!playlist || !track) return -1;
    return list_push_back(playlist, track) ? 0 : -1;
}

int playlist_remove_at(List * playlist, size_t index) {
    if (!playlist) return -1;
    return list_remove_at(playlist, index, track_free) ? 0 : -1;
}

void playlist_search_by_author(const List * playlist, const char* query, List * out_results) {
    list_init(out_results);
    if (!playlist || !query) return;
    const ListNode* cur = playlist->head;
    while (cur) {
        Track* t = (Track*)cur->data;
        if (t && contains_icase(t->author, query)) {
            list_push_back(out_results, t);
        }
        cur = cur->next;
    }
}

void playlist_search_by_title(const List * playlist, const char* query, List * out_results) {
    list_init(out_results);
    if (!playlist || !query) return;
    const ListNode* cur = playlist->head;
    while (cur) {
        Track* t = (Track*)cur->data;
        if (t && contains_icase(t->title, query)) {
            list_push_back(out_results, t);
        }
        cur = cur->next;
    }
}