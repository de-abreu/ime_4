from timeit import Timer


def empty():
    return


def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


def main():
    t0 = Timer("empty()", "from __main__ import empty")
    t0 = t0.timeit(number=1000)

    t1 = Timer("test1()", "from __main__ import test1")
    print("Concatenation:     ", t1.timeit(number=1000) - t0, "milliseconds")
    t2 = Timer("test2()", "from __main__ import test2")
    print("Appending:         ", t2.timeit(number=1000) - t0, "milliseconds")
    t3 = Timer("test3()", "from __main__ import test3")
    print("List comprehension:", t3.timeit(number=1000) - t0, "milliseconds")
    t4 = Timer("test4()", "from __main__ import test4")
    print("List range:        ", t4.timeit(number=1000) - t0, "milliseconds")


main()
