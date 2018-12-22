from array import array
from random import random

"""
 - Especially good when dealing with numbers exclusively.

 - Supports all mutable sequence operators,
   (like .pop, .insert, .extend)

 - Includes additional methods for fast saving and loading,
   such as, .frombytes and .tofile
"""

floats = array('d', (random() for i in range(10 ** 7)))
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10 ** 7)
fp.close()
print(floats2[-1])
print(floats2 == floats)

"""
 Memory Views -
    the built-in 'memoryview' class is a shared memory
    sequence type that lets you handle slices of array
    without copying bytes.
"""

# Ex. Changing the value of an array item by poking one of its bytes.
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)
