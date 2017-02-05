import random
from sort import quicksort


def test_quicksort_reverse():
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    a_quicksort = quicksort(array)
    a_baseline = sorted(array)

    assert a_baseline == a_quicksort, 'not sorted\n{0}'.format(a_quicksort)


def test_quicksort_sorted():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a_quicksort = quicksort(array)
    a_baseline = sorted(array)

    assert a_baseline == a_quicksort, 'not sorted\n{0}'.format(a_quicksort)


def test_quicksort_empty():
    array = []
    a_quicksort = quicksort(array)
    a_baseline = sorted(array)

    assert a_baseline == a_quicksort, 'not sorted\n{0}'.format(a_quicksort)


def test_quicksort_large():
    array = [random.random() for _ in xrange(100000)]
    a_quicksort = quicksort(array)
    a_baseline = sorted(array)

    assert a_baseline == a_quicksort, 'not sorted\n{0}'.format(a_quicksort)
