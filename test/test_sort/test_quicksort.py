from sort import quicksort


def test_quicksort():
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    a_quicksort = quicksort(array)
    a_baseline = sorted(array)

    assert a_baseline == a_quicksort, 'not sorted\n{0}'.format(a_quicksort)
