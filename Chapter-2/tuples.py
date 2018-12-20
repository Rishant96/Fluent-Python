import os
"""
 Tuples can be used as,
 1. Immutable lists
 2. Records with no field names
"""

# 1 - Tuples as records (here the order is vital)

lax_coordinates = (33.9425, -118.408056)  # 1
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)  # 2
traveler_ids = [('USA', '31195855'), ('BRA', 'CE542567')  # 3
                ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):  # 4
    print("%s/%s" % passport)  # 5

for country, _ in traveler_ids:  # 6
    print(country)

"""
 1 - Latitude and longitude of the Los Angeles International Airport.
 2 - Data about Tokyo: name, year, population (millions), population
     change (%), area(km sq.)
 3 - A list of tuples of the form (country_code, passport_number).
 4 - As we iterate over the list, passport is bound to each tuple.
 5 - The '%' formatting operator understands tuples and treats each
     item as a sperate field.
 6 - The 'for' loop knows how to retrieve the items of a tuple seperately;
     this is called 'unpacking'. Here we are not interested in the second
     item, so it's assigned to _, a dummy variable.
"""

# Why use tuple as records? Ans. Because of tuple unpacking mechanism.
# ------------------------------------------------------------------------

"""
 Tuple unpacking mechanism:
    
    Earlier we assigned ('Tokyo', 2003, 32450, 0.66, 8014) to city, year,
    pop, chg, area in a single statement. Then, in the last line, the %
    operator assigned each item in the passport tuple to one slot in the
    format string in the print argument.

    Those two are examples of 'tuple unpacking'.

    *
      Tuple unpacking works with any iterable object.The only
      requirement is that the iterable yields exactly one item
      per variable in the recieving tuple (unless you use '*'
      to capture excess items).
    *
"""

# Most visibile form of tuple/iterator unpacking is 'parallel algorithm'
# ie, assigning items from an iterable to a tuple of variables:
lax_coordinates = (33.9452, -118.408056)

latitude, longitude = lax_coordinates  # tuple unpacking

# 1 - an elegant application of tuple unpacking is swapping the values of
#   variables without using a temporary variable:
a, b = 5, 3  # init
b, a = a, b  # swap

# 2 - Another example of tuple unpacking is prefixing an argument with a
#   star when calling a function.
if __name__ == '__main__':
    print(divmod(20, 8))

    t = (20, 8)
    print(divmod(*t))

    quotient, remainder = divmod(*t)
    print(quotient, remainder)

# 3 - Enabling functions to return multiple values in a way that
#   is convenient to the caller.

_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)
