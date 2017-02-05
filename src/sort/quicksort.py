
def partition(A, start, end):
    pivot = start
    for i in range(start+1, end+1):
        if A[i] < A[start]:
            pivot += 1
            A[i], A[pivot] = A[pivot], A[i]
    A[pivot], A[start] = A[start], A[pivot]
    return pivot


def quicksort(A, start=0, end=None):
    if end is None:
        end = len(A) - 1
    if start < end:
        pivot = partition(A, start, end)
        quicksort(A, start, pivot-1)
        quicksort(A, pivot+1, end)
    return A
