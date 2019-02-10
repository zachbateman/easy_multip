from easy_multip.decorators import use_multip
import time
import random


# first_arg = [i for i in range(20000000)]
# first_arg = [i for i in range(10)]
first_arg = [i for i in range(5000)]


def test_func(list_arg, arg2, arg3, add=True):
    results = []
    for x in list_arg:
        time.sleep(0.001)
        if add:
            results.append(x + arg2 + arg3)
        else:
            results.append(x - arg2 - arg3)
    return results


@use_multip
def test_decorator_func(list_arg, arg2, arg3, add=True):
    results = []
    for x in list_arg:
        time.sleep(0.001)
        if add:
            results.append(x + arg2 + arg3)
        else:
            results.append(x - arg2 - arg3)
    return results
    
# test_decorator_func2 = use_multip(test_decorator_func)


if __name__ == '__main__':
    t0 = time.time()
    results = test_func(first_arg, 3, 4, add=False)
    print(f'Normal function time: {round(time.time() - t0, 2)}')

    t0 = time.time()
    results2 = test_decorator_func(first_arg, 3, 4, add=False)
    print(f'@use_multip decorated time: {round(time.time() - t0, 2)}')
    
    # t0 = time.time()
    # results2 = test_decorator_func2(first_arg, 3, 4, add=False)
    # print(f'@use_multip decorated time: {round(time.time() - t0, 2)}')

    if results2 != results:
        print('ERROR!!! Different output from test_func and test_decorator_func!!!')
        print(results)
        print(results2)
