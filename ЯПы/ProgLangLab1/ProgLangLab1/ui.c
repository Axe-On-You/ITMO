#include "ui.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>

static void trim_newline(char* s) {
    if (!s) return;
    size_t len = strlen(s);
    while (len > 0 && (s[len - 1] == '\n' || s[len - 1] == '\r')) {
        s[--len] = '\0';
    }
}

static void read_line(const char* prompt, char* buf, size_t bufsz) {
    if (prompt) printf("%s", prompt);
    if (!fgets(buf, (int)bufsz, stdin)) {
        if (bufsz > 0) buf[0] = '\0';
        return;
    }
    trim_newline(buf);
}

static int read_int_line(const char* prompt, int* out_val) {
    char tmp[128];
    read_line(prompt, tmp, sizeof(tmp));
    if (tmp[0] == '\0') return -1;
    char* end = NULL;
    long v = strtol(tmp, &end, 10);
    if (end == tmp) return -1;
    *out_val = (int)v;
    return 0;
}

static void print_playlist(void* ctx, const UiOps* ops) {
    const List* playlist = NULL;
    ops->get_all(ctx, &playlist);
    size_t n = list_size(playlist);
    if (n == 0) {
        printf("Плейлист пуст.\n");
        return;
    }
    const ListNode* cur = playlist->head;
    long idx = 1;
    char row[512];
    while (cur) {
        ops->format_item_row(ctx, cur->data, idx, row, sizeof(row));
        printf("%s\n", row);
        cur = cur->next;
        ++idx;
    }
}

static void add_track_flow(void* ctx, const UiOps* ops) {
    char author[128];
    char title[128];
    char dur_in[64];

    printf("Добавление композиции\n");
    read_line("Автор: ", author, sizeof(author));
    read_line("Название: ", title, sizeof(title));
    read_line("Длительность (мм:сс или секунды): ", dur_in, sizeof(dur_in));

    int rc = ops->add(ctx, author, title, dur_in);
    if (rc == 0) {
        printf("Композиция добавлена.\n");
    }
    else {
        printf("Ошибка: не удалось добавить композицию (код %d).\n", rc);
    }
}

static void remove_track_flow(void* ctx, const UiOps* ops) {
    const List* playlist = NULL;
    ops->get_all(ctx, &playlist);
    if (list_size(playlist) == 0) {
        printf("Плейлист пуст.\n");
        return;
    }
    print_playlist(ctx, ops);
    int num = 0;
    if (read_int_line("Введите номер для удаления: ", &num) != 0 || num <= 0) {
        printf("Ошибка: введите корректный номер.\n");
        return;
    }
    int rc = ops->remove_by_number(ctx, (size_t)num);
    if (rc == 0) {
        printf("Композиция удалена.\n");
    }
    else {
        printf("Ошибка: не удалось удалить (код %d).\n", rc);
    }
}

static void search_flow(void* ctx, const UiOps* ops) {
    const List* playlist = NULL;
    ops->get_all(ctx, &playlist);
    if (list_size(playlist) == 0) {
        printf("Плейлист пуст.\n");
        return;
    }
    printf("Поиск по критерию:\n");
    printf("1. Автор\n");
    printf("2. Название\n");
    int choice = 0;
    if (read_int_line("> ", &choice) != 0 || (choice != 1 && choice != 2)) {
        printf("Ошибка: выберите 1 или 2.\n");
        return;
    }
    char query[128];
    read_line("Строка поиска: ", query, sizeof(query));
    if (query[0] == '\0') {
        printf("Пустой запрос.\n");
        return;
    }

    List results;
    if (choice == 1) ops->search_by_author(ctx, query, &results);
    else            ops->search_by_title(ctx, query, &results);

    size_t cnt = list_size(&results);
    if (cnt == 0) {
        printf("Ничего не найдено.\n");
        list_clear(&results, NULL);
        return;
    }
    printf("Найдено: %zu\n", cnt);

    const ListNode* cur = results.head;
    char row[512];
    while (cur) {
        const void* item = cur->data;
        long idx = list_index_of(playlist, item);
        if (idx >= 0) {
            ops->format_item_row(ctx, item, idx + 1, row, sizeof(row));
            printf("%s\n", row);
        }
        cur = cur->next;
    }
    list_clear(&results, NULL);
}

void run_ui(void* ctx, const UiOps* ops) {
    printf("Введите номер действия и нажмите [Enter]. Затем следуйте инструкциям.\n");
    for (;;) {
        printf("\nМеню:\n");
        printf("1. Поиск\n");
        printf("2. Показать все композиции\n");
        printf("3. Добавить композицию\n");
        printf("4. Удалить композицию\n");
        printf("5. Выход\n");
        int cmd = 0;
        if (read_int_line("> ", &cmd) != 0) {
            printf("Некорректный ввод. Повторите.\n");
            continue;
        }
        switch (cmd) {
        case 1: search_flow(ctx, ops); break;
        case 2: print_playlist(ctx, ops); break;
        case 3: add_track_flow(ctx, ops); break;
        case 4: remove_track_flow(ctx, ops); break;
        case 5: return;
        default: printf("Выберите пункт 1-5.\n"); break;
        }
    }
}