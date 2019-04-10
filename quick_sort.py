def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        lesser = [i for i in a[1:] if i < pivot]
        greater = [i for i in a[1:] if i >= pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)
