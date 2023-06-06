#include "lists.h"

/**
 * *insert_node - Function that add a node to a list
 * @head: pointer to the first node
 * @number: number
 * Return: Return null || new node
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *crr = *head;
listint_t *new_node;

new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);
new_node->n = number;

if (crr == NULL || crr->n >= number)
{
new_node->next = crr;
*head = new_node;
return (new_node);
}

while (crr && crr->next && crr->next->n < number)
crr = crr->next;

new_node->next = crr->next;
crr->next = new_node;

return (new_node);
}
