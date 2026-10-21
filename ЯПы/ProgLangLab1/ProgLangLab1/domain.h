#ifndef DOMAIN_H
#define DOMAIN_H

#include "collections.h"
#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

    typedef struct Track {
        char author[128];
        char title[128];
        int duration_sec;
    } Track;

    Track* track_new(const char* author, const char* title, int duration_sec);
    void   track_free(void* p);

    char* track_format_duration(int sec, char* buf, size_t bufsize);
    int   track_parse_duration(const char* s, int* out_sec);

    int playlist_add_track(List* playlist, Track* track); 
    int playlist_remove_at(List* playlist, size_t index);
    void playlist_search_by_author(const List* playlist, const char* query, List* out_results);
    void playlist_search_by_title(const List* playlist, const char* query, List* out_results);

#ifdef __cplusplus
}
#endif

#endif