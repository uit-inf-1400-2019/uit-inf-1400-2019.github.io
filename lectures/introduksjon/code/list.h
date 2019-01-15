#ifndef LIST_H_
#define LIST_H_

/*
 * List interface
 */

struct list;
typedef struct list list_t;

// Create new list
list_t *list_create(void);

// Free list. All nodes are freed, but not items pointed to by nodes.
void list_destroy(list_t *list);

// Insert item first in list
int list_addfirst(list_t *list, void *item);

// Insert item last in list
int list_addlast(list_t *list, void *item);

// Remove object from list
void list_remove(list_t *list, void *item);

// Return # of items in list
int list_size(list_t *list);


/*
 * List iterator interface
 */
 
struct list_iterator;
typedef struct list_iterator list_iterator_t;

// Create new list iterator
list_iterator_t *list_createiterator(list_t *list);

// Free iterator
void list_destroyiterator(list_iterator_t *iter);

// Move iterator to next item and return current
void *list_next(list_iterator_t *iter);

// Let iterator point to first item in list
void list_resetiterator(list_iterator_t *iter);

#endif /*LIST_H_*/
