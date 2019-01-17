import easy_multip
import time
import random

args = [(1,2), (3,5), (6,2), (7,0), (7,1), (8,5), (5,2), (8,8), (4,7), (1,6), (1,1), (2,2), (6,6), (7,4), (7,3), (5,5)]

def test_func(x, y):
    time.sleep(random.random() * 2)
    print(x + y)


if __name__ == '__main__':
    t0 = time.time()
    for arg in args:
        test_func(*arg)
    print(f'Normal loop time: {round(time.time() - t0, 2)}')

    t0 = time.time()
    easy_multip.doloop(test_func, args)
    print(f'easy_multip.doloop time: {round(time.time() - t0, 2)}')
