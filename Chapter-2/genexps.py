import array
"""
 To initialize tuples, arrays and other types of sequences,
 you could also start from a listcomp but a genexp saves
 memory because it yields items one-by-one using the iterator
 protocol instead of building a whole list just to feed
 another constructor.
"""
# Genexps use the same syntax as listcomps, but are
# enclosed in parenthesis rather than brackets.

# Simple Example - genexp

symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)  # 1
array.array('I', (ord(symbol) for symbol in symbols))  # 2
# The first argument defines the storage type.

"""
 1 - If the generator expression is the single argument in a
     function call, there is no need to duplicate the enclosing
     parenthesis.

 2 - The array constructor takes two arguments, so the parenthesis
     around the generator expression are mandatory.
 """

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):  # 1
    print(tshirt)
"""
 The generator expression yields items one by one; a list with all 6
 t-shirt variations is never produced in this example.
"""
