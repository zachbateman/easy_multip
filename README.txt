
easy_multip Python Package
Zach Bateman

This small utility is designed to quickly and allow multiprocessing
capabilities while greatly simplifying code for easier use.

Initial capabilities:
 -- easy_multip.map(func, x_group)
    
    map() or "list comprehension" type functionality that is
    EASILY parallelized using multiprocessing and includes a progress bar.

    This is for creating lists similar to the below constructs:

            list(map(func, x_group))
                    or
            [func(x) for x in x_group]
