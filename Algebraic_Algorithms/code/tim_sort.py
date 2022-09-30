if __name__ == '__main__':
    import cProfile
    import random
    N = 10000

    test_container = [random.random() for _ in range(N)]

    pr = cProfile.Profile()
    pr.enable()
    sorted(test_container)
    pr.disable()
    pr.print_stats()