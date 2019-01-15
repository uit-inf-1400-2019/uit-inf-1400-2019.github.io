#include <stdio.h> 

class ListNode {} ; 

class List {
    ListNode  *head; 
    int numItems; 
    
    int add(void *item) {
	return addLast(item); 
    }
    int addLast(void *item); 
}; 

int List::addLast(void *item) 
{
}

int main() 
{
    return 0; 
}
