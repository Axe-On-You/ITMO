#include "collections.h"
#include <stdlib.h>

void list_init(List* list) {
    list->head = NULL;
    list->tail = NULL;
    list->size = 0;
}

void list_clear(List* list, free_fn free_data) {
    ListNode* cur = list->head;
    while (cur) {
        ListNode* next = cur->next;
        if (free_data && cur->data) free_data(cur->data);
        free(cur);
        cur = next;
    }
    list_init(list);
}

bool list_push_back(List* list, void* data) {
    ListNode* node = (ListNode*)malloc(sizeof(ListNode));
    if (!node) return false;
    node->data = data;
    node->next = NULL;
    if (!list->head) {
        list->head = list->tail = node;
    }
    else {
        list->tail->next = node;
        list->tail = node;
    }
    list->size += 1;
    return true;
}

void* list_get_at(const List* list, size_t index) {
    if (!list || index >= list->size) return NULL;
    size_t i = 0;
    const ListNode* cur = list->head;
    while (cur) {
        if (i == index) return cur->data;
        cur = cur->next;
        ++i;
    }
    return NULL;
}

bool list_remove_at(List* list, size_t index, free_fn free_data) {
    if (!list || index >= list->size) return false;
    ListNode* prev = NULL;
    ListNode* cur = list->head;
    size_t i = 0;
    while (cur) {
        if (i == index) {
            if (prev) prev->next = cur->next;
            else list->head = cur->next;
            if (cur == list->tail) list->tail = prev;
            if (free_data && cur->data) free_data(cur->data);
            free(cur);
            list->size -= 1;
            return true;
        }
        prev = cur;
        cur = cur->next;
        ++i;
    }
    return false;
}

size_t list_size(const List* list) {
    return list ? list->size : 0;
}

long list_index_of(const List* list, const void* data) {
    if (!list) return -1;
    long idx = 0;
    const ListNode* cur = list->head;
    while (cur) {
        if (cur->data == data) return idx;
        cur = cur->next;
        ++idx;
    }
    return -1;
}