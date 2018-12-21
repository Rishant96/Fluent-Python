# list.sort and the 'sorted' built-in function

"""
 list.sort v/s sorted

 - list.sort method sorts in-place, and returns 'None'
   (this is an important Python API convention:
        functions or methods that change an object in-
        place should return 'None' to make it clear to
        the caller that the object itself was changed
        and no new object was created.

      * this convention has a drawback: you cannot cascade
      the calls those methods.
    )

 - In contrast,the built-in function 'sorted' creates a new
   list and returns it,

   * 'sorted' accepts any iterable object as argument (including
      immutable sequences and generators).
      Regardless of the type of iterable given to 'sorted', it
      always returns a newly created list.

 - Both 'list.sort' and 'sorted' take two optional, keyword
   arguments: 'key' and 'reverse'.

   ('key' - A one-argument fuction that will be applied to each
            item to its sorting key.
        For example - when sorting a list of strings,
            'str.lower can be used to perform a case-insensitive
             sort, and key=len will sort the strings by character
             length.
             The default is the identity function, i.e., the items themselves
             are compared.'

        The 'key' optional keyword parameter can also be used with the 'min()'
        and 'max()' built-ins and with other functions from the standard
        library such as itertools.groupby() and heapq.nlargest().
    )
"""

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(fruits)
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
print(fruits)
print(fruits.sort())
