from easy_multip.decorators import use_multip
import time


first_arg = [i for i in range(5000)]


# decorated with "use_multip" below definition (can't use @ sugar b/c pickle issues)
def test_func(list_arg: list, arg2, arg3, add=True):
    '''
    Takes first arg as list and returns a list or None.
    '''
    results = []
    for x in list_arg:
        time.sleep(0.001)
        if add:
            results.append(x + arg2 + arg3)
        else:
            results.append(x - arg2 - arg3)
    return results
decorated_test_func = use_multip(test_func)



if __name__ == '__main__':
    t0 = time.time()
    results = test_func(first_arg, 3, 4, add=False)
    print(f'Normal function time: {round(time.time() - t0, 2)}')

    t0 = time.time()
    results2 = decorated_test_func(first_arg, 3, 4, add=False)
    print(f'use_multip decorated time: {round(time.time() - t0, 2)}')

    if results2 != results:
        print('ERROR!!! Different output from test_func and test_decorator_func!!!')
        print(results)
        print(results2)
