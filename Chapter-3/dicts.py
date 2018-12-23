import collections.abc as abc
my_dict = {}
print(isinstance(my_dict, abc.Mapping))

# Hashable test

tt = (1, 2, (30, 40))
print(hash(tt))

tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

try:
    tl = (1, 2, [30, 40])
    print(hash(tl))
except Exception as e:
    print(e)

# Ways of building a 'dict'
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)
