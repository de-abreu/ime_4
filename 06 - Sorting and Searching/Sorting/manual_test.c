#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#define array int*

void insertionSort (array A, int size, int start, int gap) {
    int i = start + gap, tmp;

	if (i >= size)
		return;
	tmp = A[i];
	while (i >= gap && A[i - gap] > tmp) {
		A[i] = A[i - gap];
		i-= gap;
	}
	A[i] = tmp;
	insertionSort(A, size, start + gap, gap);
}

void shellSort (array A, int size) {
	int i, sublist_lenght;

	for (sublist_lenght = size /2; sublist_lenght > 0; sublist_lenght /= 2)
		for (i = 0; i < sublist_lenght; i++)
	    	insertionSort(A, size, i, sublist_lenght);
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
	shellSort(A, size);

	printf("\nArranjo ordenado:\n");
	for (i = 0; i < size; i++)
		printf("%d ", A[i]);
	printf("\n");
	free(A);
    return 0;
}
