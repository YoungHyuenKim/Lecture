def merge_sort(arr):
    def _sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        _sort(low, mid)
        _sort(mid, high)
        _merge(low, mid, high)
    def _merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1
        for i in range(low, high):
            arr[i] = temp[i - low]
    return _sort(0, len(arr))


if __name__ == '__main__':
    import cProfile
    import random

    N = 1000000

    test_container = [random.random() for _ in range(N)]

    pr = cProfile.Profile()
    pr.enable()
    merge_sort(test_container)
    pr.disable()
    pr.print_stats()
