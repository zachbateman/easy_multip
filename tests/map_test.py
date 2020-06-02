import easy_multip
import time
import random
import sys
sys.path.insert(1, '..')

args = [(1,2), (3,5), (6,2), (7,0), (7,1), (8,5), (5,2), (8,8), (4,7), (1,6), (1,1), (2,2), (6,6), (7,4), (7,3), (5,5)]

def test_func(arg_tup):
    x, y = arg_tup
    time.sleep(random.random() * 2)
    return x + y


if __name__ == '__main__':
    t0 = time.time()
    data1 = [test_func(arg) for arg in args]
    print(f'Normal loop time: {round(time.time() - t0, 2)}')

    t0 = time.time()
    data2 = easy_multip.map(test_func, args)
    print(f'easy_multip.doloop time: {round(time.time() - t0, 2)}')
    
    print(f'data1 == data2 check: {data1 == data2}')
