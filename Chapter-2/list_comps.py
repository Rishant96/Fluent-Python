"""
 List comprehension
"""

# Ex. 1 - Showcasing readibility advantages of list-comps

symbols = '$¢£¥€¤'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))

# versus

codes_comp = [ord(symbol) for symbol in symbols]

"""-------------------------------------------------------"""

# Ex. 2 - Listcomp versus a map/filter comprehension

symbols = '$¢£¥€¤'

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
"""
 >>> beyond_ascii
 [162, 163, 165, 8364, 164]
"""

# versus

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))

"""-----------------------------------------------------------"""

# Cartesian products

#   Ex: list shirts available in 2 colors and 3 sizes.

colors = ["black", "white"]
sizes = ['S', 'M', 'L']

#     Method - 1
tshirts = [(color, size) for color in colors for size in sizes]

#     Method - 2
for color in colors:
    for size in sizes:
        print((color, size))

#     Method - 3
tshirts = [(color, size) for size in sizes
                         for color in colors]

# -------------------------------------------------------------

"""
 Conclusion:

   - Listcomps are a one-trick pony: they build lsits.
     (To fill-up other sequence types, a genexp is the way to go)
"""
