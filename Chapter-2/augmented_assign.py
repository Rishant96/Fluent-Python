# Augmented assignment with squences

# Focusing on '+=', but concepts apply to all

# special method for '+=' is '__iadd__'("in-place add")
# however if '__iadd__' is not implemented, then python
# uses '__add__' as a fallback.

a, b = [2, 3], [5, 6, 7]
a += b
print(a)

"""
 If 'a' implements __iadd__, that will be called.

 In case of mutable sequences like 'list', 'bytearray',
 'array.array', etc. 'a' will be changed in-place, i.e.
 the effect will be similar to a.extend(b).

 However, when 'a' does not implement '__iadd__', the
 expression 'a += b' has the same as a = a + b: the expression
 a + b is evaluated first, producing a new object which is then
 bound to 'a'.

 In other words, the identity of the object bound to 'a' may or
 may not change, depending on the availability of '__iadd__'.

 In general, for mutable sequences it is a good bet that '__iadd__'
 is implemented and that '+=' happens in-place.
 For immutable sequences, clearly there is no way for that to happen.
"""

# Example
s = [1, 2, 3]
print(id(s))
s *= 2
print(id(s))
t = (1, 2, 3)
print(id(t))
t *= 2
print(id(t))

# Corner case for '+=': tuple with mutable element, assigning value
