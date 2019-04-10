def qsort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        lesser = [i for i in a[1:] if i < pivot]
        greater = [i for i in a[1:] if i >= pivot]
    return qsort(lesser) + [pivot] + qsort(greater)
