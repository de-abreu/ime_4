def bubble_sort(l):
    size = len(l)

    while size > 1:
        size -= 1
        for i in range(size):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
    return l
