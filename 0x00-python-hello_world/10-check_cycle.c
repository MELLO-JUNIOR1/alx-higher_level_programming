#include "lists.h"

/**
* check_cycle - Function that check if there is a cycle in a list
* @list: the list
* Return: Return 0 || -1
*/

int check_cycle(listint_t *list)
{
listint_t *slow, *fast;

slow = fast = list;

while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}
return (0);
}
