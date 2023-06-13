#include "lists.h"

/**
 * is_palindrome - Function to check if the list is palindrom
 * @head: pointer
 * Return: Return 1 || 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *curr = *head;
	listint_t *rev = *head;
	int count = 0, i = 0, j = 0;

	if (!*head)
		return (1);

	while (curr)
	{
	curr = curr->next;
	count++;
	}
	curr = *head;
	for (i = 1; i <= count; i++)
	{
	for (j = i; j <= count - i; j++)
		rev = rev->next;
	if (curr->n != rev->n)
		return (0);
	curr = curr->next;
	rev = curr;
	}
return (1);
}
