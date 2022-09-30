def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == '__main__':
    import cProfile
    import random

    N = 10000

    test_container = [random.random() for _ in range(N)]

    pr = cProfile.Profile()
    pr.enable()
    selection_sort(test_container)
    pr.disable()
    pr.print_stats()
