# easy_multip

easy_multip is a small tool designed to quickly allow Python multiprocessing capabilities while greatly simplifying code for easier use.

# Current Features

  - easy_multip.map(func, arg_group, leave_one_cpu_free=False)
    - map() or list comprehension type functionality that is parallelized using multiprocessing and includes a progress bar
    - Usage is similar to the below constructs:
        ```sh
        list(map(func, arg_group))
            or
        [func(arg) for arg in arg_group]
        ```
  - easy_multip.doloop(func, arg_group, leave_one_cpu_free=False)
    - for loop equivalent that runs a function that returns None
    - Useful in situations like file processing where each operation is expensive and totally independant
    - Allocates jobs evenly among processors and provides a progress bar... of sorts
    - Usage is similar to the below construct:
        ```sh
        for arg in arg_group:
            func(arg)
        ```

License
----
MIT
