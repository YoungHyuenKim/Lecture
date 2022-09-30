def merge_sort_slow(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort_slow(arr[:mid])
    high_arr = merge_sort_slow(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


if __name__ == '__main__':
    import cProfile
    import random
    N = 10000

    test_container = [random.random() for _ in range(N)]

    pr = cProfile.Profile()
    pr.enable()
    merge_sort_slow(test_container)
    pr.disable()
    pr.print_stats()