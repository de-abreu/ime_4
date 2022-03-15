#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#define array int*

void swap (int *a, int *b) {
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

int * median(int *a, int *b, int *c) {
	if ((*a > *b) ^ (*a > *c))
		return a;
	if ((*b < *a) ^ (*b < *c))
		return b;
	return c;
}

int partition (array A, int size) {
	int i, j, last = size - 1;

	swap(&A[last], median(A, A + size / 2, A + last));
	for (i = j = 0; i < last; i++)
	    if (A[i] <= A[last])
			swap(&A[i], &A[j++]);
	swap(&A[i], &A[j]);
	return j;
}

void quickSort (array A, int size) {
	int pivot;

	if (size <= 1)
		return;
	pivot = partition(A, size);
	quickSort(A, pivot++);
	quickSort(A + pivot, size - pivot);
}

int * readArray (int *size) {
	int d, i = 0;
	char c;
	array A;

	*size = 1;
	A = malloc(sizeof(int));
	do {
		if (!scanf(" %d", &d))
			continue;
		if (i == *size - 1) {
			*size *= 2;
			A = realloc(A, *size * sizeof(int));
		}
		A[i++] = d;
	} while ((c = getchar()) != EOF && c != '\n');
	*size = i;
	return A;
}

int main () {
    int i, size;
	array A;

	printf("Este programa admite uma lista de valores inteiros x tais que %d ≤ x ≤ %d e os ordena em ordem creescente.\nDigite uma série de valores inteiros separadas entre si por espaço e pressione ENTER:\n", INT_MIN, INT_MAX);
	A = readArray(&size);
	quickSort(A, size);

	printf("\nArranjo ordenado:\n");
	for (i = 0; i < size; i++)
		printf("%d ", A[i]);
	printf("\n");
	free(A);
    return 0;
}
