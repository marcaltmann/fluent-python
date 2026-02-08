"""
sort() method and sorted()
What can I learn here?
Mostly about the use of key functions and lambdas.
Also about the Python principle that a method just returns None
when no new object is created and the object has been changed, e.g.
a.sort() returns None.
"""

a = [8, 3, 5, 1, 0]

print(sorted(a))

print(a)

result = a.sort()
print(result)

print(a)

a.sort(reverse=True)
print(a)


tuples = [('b', 50), ('c', 25), ('a', 100)]

# Automatically sorts according to first element of each tuple.
print(sorted(tuples))

# Manually do the same thing.
print(sorted(tuples, key=lambda x: x[0]))

# Sort by the second element of each tuple.
print(sorted(tuples, key=lambda x: x[1]))
