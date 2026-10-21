#ifndef UI_H
#define UI_H

#include "collections.h"
#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

    typedef struct UiOps {
        void (*get_all)(void* ctx, const List** out_list);
        int (*add)(void* ctx, const char* author, const char* title, const char* duration_str);
        int (*remove_by_number)(void* ctx, size_t one_based_index);
        void (*search_by_author)(void* ctx, const char* query, List* out_results);
        void (*search_by_title) (void* ctx, const char* query, List* out_results);
        void (*format_item_row)(void* ctx, const void* item, long one_based_index, char* out, size_t outsz);
    } UiOps;

    void run_ui(void* ctx, const UiOps* ops);

#ifdef __cplusplus
}
#endif

#endif