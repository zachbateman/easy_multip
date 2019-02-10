'''
Module containing easy_multip decorators.
'''
# from .functions import maps as multip_map
from .functions import _num_cpus
import multiprocessing
from multiprocessing import Process, Manager
import functools
from functools import wraps
import tqdm
import math
from pprint import pprint as pp


def use_multip(func, leave_one_cpu_free=True, verbose: bool=False):
    '''
    Decorator providing capability to quickly use multiprocessing with
    an expensive function operating on a list.
    
    CAUTION:  To be used ONLY with functions taking a list first arg which is
    operated on by all the other (optional) args and that return another list or None.
    '''
    
    
    @wraps(func)  # allows for decorated function's docstring to come through decorator
    def inner(*args, **kwargs):
        try:
            first_arg = args[0]
        except:
            raise ValueError(f'{func.__name__} needs a list arg when using the @use_multip decorator.')
        if type(first_arg) == list:
            pass
        else:
            raise TypeError(f'The first arg of {func.__name__} must be a list when using the @use_multip decorator.') 
        
        num_cpus = _num_cpus(leave_one_cpu_free)
        
        chunk_size = math.ceil(len(first_arg) / num_cpus)  # round UP
        sublists = [first_arg[cpu_index * chunk_size:(cpu_index + 1) * chunk_size] for cpu_index in range(num_cpus)]
        
        with Manager() as manager:
            result_dict = manager.dict()  # dict-ish thing handling dict-like data storage among processes

            processes = [Process(target=_use_multip_worker,
                                 args=(func, sublists[i], i, result_dict, args[1:], kwargs))
                                    for i in range(num_cpus)]

            for proc in processes:
                proc.start()
            for proc in processes:
                proc.join()
        
            returned = []
            for i in range(num_cpus):
                returned.extend(result_dict[i])

        if all(x is None for x in returned):
            return None
        else:
            return returned
    
    inner.__name__ = '__main__.' + inner.__name__
    
    
    # functools.update_wrapper(inner, func)
    return inner


    
def _use_multip_worker(func, sublist, cpu_index, working_dict, *args):
    '''
    This worker function must be at the top-level of this module
    so that it can be pickled for multiprocessing.
    '''
    args, kwargs = args  # both are coming in as *args
    # for item_dict in tqdm.tqdm(sublist):
    working_dict[cpu_index] = func(sublist, args[0], args[1], **kwargs)
    
        # for index, item in item_dict.items():  # there will only be one index:item pair
            # working_dict[index] = func(item, args, kwargs)

    
# def _master_func(func, first_arg, *args, **kwargs):
    # '''   '''
    # return func((first_arg, *args, **kwargs))


