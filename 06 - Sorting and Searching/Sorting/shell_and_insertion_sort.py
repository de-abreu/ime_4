def shell_sort(l):
    sublist_lenght = len(l) // 2
    while sublist_lenght > 0:
        for i in range(sublist_lenght):
            l = insertion_sort(l, i, sublist_lenght)
        sublist_lenght //= 2
    return l

def insertion_sort(l, start=0, gap=1):
    for i in range(start + gap, len(l), gap):
        tmp = l[i]
        j = i
        while j >= gap and l[j - gap] > tmp:
            l[j] = l[j - gap]
            j -= gap
        l[j] = tmp
    return l
