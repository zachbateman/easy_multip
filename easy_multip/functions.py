'''
Module containing easy_multip functions.
'''
import multiprocessing
from multiprocessing import Process, Manager
import tqdm


def map(expensive_func, iterable, leave_one_cpu_free=False):
    '''
    Equivalent usage to the map() function for use with expensive
    functions operating on iterable.

    Runs these operations in parallel on the max number of processes for the job,
    and maintains the same resulting index order as a normal map() or
    list comprehension usage.

    NOTE: This implementation appears FASTER than normal multiprocessing.Pool.map()!
          The reason is likely because the jobs are distributed as evenly as possible
          among the proceses whereas in normal map, one process might get all of the
          remaining jobs if the job count is not cleanly divisible by processor count.

          (Example, for 100 jobs on 8 processors has each processor running 12 or 13 jobs
          instead of 7 doing 12 jobs and one doing 16 jobs.)

    leave_one_cpu_free arg can be set as True to not use ALL the computer's resources.
    '''
    num_cpus = multiprocessing.cpu_count()
    if leave_one_cpu_free and num_cpus > 1:
        num_cpus -= 1

    iterable_index_dicts = [{index: item} for index, item in enumerate(iterable)]  # used for list order
    with Manager() as manager:
        result_dict = manager.dict()  # dict-ish thing handling dict-like data storage among processes

        # next 3 lines most evenly spread out data args into groups for processes
        # does NOT matter that they are not in order, as the "index" in each
        # iterable_index_dict handles ordering of results at the end!
        iterable_groups = [[] for _ in range(num_cpus)]
        for i, index_dict in enumerate(iterable_index_dicts):
            iterable_groups[i % (num_cpus)].append(index_dict)

        processes = [Process(target=multiprocessing_worker,
                             args=(expensive_func, iterable_groups[i], result_dict))
                                for i in range(num_cpus)]
        print(f'---easy_multip.map started---')
        print(f'Firing up {num_cpus} processes.')
        print(f'The below progress bar switches between individual processes.')

        for proc in processes:
            proc.start()
        for proc in processes:
            proc.join()

        return [result_dict[i] for i in range(len(iterable))]


def multiprocessing_worker(func, iterable_sublist, working_dict):
    '''
    This worker function must be at the top-level of this module
    so that it can be pickled for multiprocessing.
    '''
    for item_dict in tqdm.tqdm(iterable_sublist):
        for index, item in item_dict.items():  # there will only be one index:item pair
            working_dict[index] = func(item)
