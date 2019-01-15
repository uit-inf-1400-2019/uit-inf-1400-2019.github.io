#include <stdio.h>
#include <stdlib.h>
#include "list.h"


/*
 * List implementation
 */

typedef struct listnode listnode_t;
struct listnode {
    listnode_t  *next;
    void        *item;
};

struct list {
    listnode_t *head;
    int numitems;
};


// Create new list
list_t *list_create(void)
{
    list_t *list;

    list = (list_t*)malloc(sizeof(list_t));
    if (list == NULL)
        goto error;
    list->head = NULL;
    list->numitems = 0;

    return list;
 error:
    return NULL;
}

// Free list. items not freed.
void list_destroy(list_t *list)
{
    listnode_t *node, *tmp;

    node = list->head;
    while (node != NULL) {
        tmp = node->next;
        free(node);
        node = tmp;
    }
    free(list);
}


// Create new list node.  Function declared static => only visible within this file
static listnode_t *list_newnode(void *item)
{
    listnode_t *node;

    node = (listnode_t*)malloc(sizeof(listnode_t));
    if (node == NULL)
        goto error;
    node->next = NULL;
    node->item = item;

    return node;
 error:
    return NULL;
}


// Insert item first in list
int list_addfirst(list_t *list, void *item)
{
    listnode_t *node;

    node = list_newnode(item);
    if (node == NULL)
        goto error;

    if (list->head != NULL)
        node->next = list->head;
    list->head = node;
    list->numitems++;

    return 0;
 error:
    return -1;
}


// Insert item last in list.
int list_addlast(list_t *list, void *item)
{
    listnode_t *node, *current;

    node = list_newnode(item);
    if (node == NULL)
        goto error;

    current = list->head;
    if (current == NULL) {
        list->head = node;
    } else if (current->next == NULL) {
        current->next = node;
    } else {
        while (current->next->next != NULL)
            current = current->next;
        current->next->next = node;
    }
    list->numitems++;

    return 0;
 error:
    return -1;
}


// Remove item from list
void list_remove(list_t *list, void *item)
{
    listnode_t *current;

    current = list->head;
    if (current == NULL) {
        goto done;
    } else if (current->item == item) {
        list->head = current->next;
    } else {
        while (current->next != NULL) {
            if (current->next->item == item) {
                current->next = current->next->next;
                break;
            }
            current = current->next;
        }
    }
    list->numitems--;

done:
    return;
}


// Return # of items in list
int list_size(list_t *list)
{
    return list->numitems;
}



/*
 * Iterator implementation
 */


struct list_iterator {
    listnode_t *next;
    list_t *list;
};


// Create new list iterator
list_iterator_t *list_createiterator(list_t *list)
{
    list_iterator_t *iter;

    iter = (list_iterator_t*)malloc(sizeof(list_iterator_t));
    if (iter == NULL)
        goto error;

    iter->list = list;
    iter->next = list->head;

    return iter;
 error:
    return NULL;
}


// Free iterator
void list_destroyiterator(list_iterator_t *iter)
{
    free(iter);
}


// Move iterator to next item in list and return current.
void *list_next(list_iterator_t *iter)
{
    void *item;

    item = NULL;
    if (iter->next != NULL) {
        item = iter->next->item;
        iter->next = iter->next->next;
    }

    return item;
}


// Let iterator point to first item in list again
void list_resetiterator(list_iterator_t *iter)
{
    iter->next = iter->list->head;
}

// Check if end of list is reached
int list_hasnext(list_iterator_t *iter)
{
	if (iter->next != NULL)
		return 1;

	return 0;
}

