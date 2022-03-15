def min_index(l, start):
    pos = start

    for i in range(start + 1, len(l)):
        if l[i] < l[pos]:
            pos = i
    return pos


def selection_sort(l):
    for i in range(len(l) - 2):
        min = min_index(l, i)
        l[i], l[min] = l[min], l[i]
    return l
