import bisect
import sys
import random

"""
 The 'bisect' module offers two functions
 -- 'bisect' and 'insort'
"""

# Searching with 'bisect':

"""
 bisect(haystack, needle) - finds the position where
     needle can be inserted in the haystack, while
     maintaining haystack in ascending order.
"""

# Example: 'bisect' finds insertion points for items in
#   a sorted sequence.

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d}  @ {1:2d}   {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

# Example 2: using 'bisect' to perform table lookups by numeric
#     values. in particular, to convert test scores to grades...


def grade(score, breakpoints=[60, 70, 80, 90],
                 grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


print([grade(score) for score in [60, 33, 99, 77, 70, 89, 90, 100]])

"""
 insort(seq, item): inserts 'item' into 'seq' so as to keep 'seq'
 in ascending order.
"""

# Insort keeps a sorted sequence always sorted.

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
