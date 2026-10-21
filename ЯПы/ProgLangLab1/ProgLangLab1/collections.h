#ifndef COLLECTIONS_H
#define COLLECTIONS_H

#include <stddef.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

    typedef void (*free_fn)(void*);

    typedef struct ListNode {
        void* data;
        struct ListNode* next;
    } ListNode;

    typedef struct List {
        ListNode* head;
        ListNode* tail;
        size_t size;
    } List;

    void list_init(List* list);
    void list_clear(List* list, free_fn free_data);
    bool list_push_back(List* list, void* data);
    void* list_get_at(const List* list, size_t index);
    bool list_remove_at(List* list, size_t index, free_fn free_data);
    size_t list_size(const List* list);
    long list_index_of(const List* list, const void* data); // -1 если не найдено

#ifdef __cplusplus
}
#endif

#endif