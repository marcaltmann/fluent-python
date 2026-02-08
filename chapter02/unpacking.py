"""
Tuple unpacking.
Overly complicated...

Generally, parentheses can be omitted, e.g.
"""

a = 1
b = 2
(a, b)
a, b

"""
If the tuple contains only one element, add trailing comma:
This design decision shows that tuples are rather important in Python...
"""
(1,)
(1,)

"""
So, you can unpack to variables (in a tuple! weird...).
It really is a tuple of variables. Called 'parallel assignment'.
"""
a, b = (1, 2)

"""
And also you can capture the rest of the tuple in one variable with preceding star:
Not only at the end.
"""
a, *b = (1, 2, 3)
*a, b = (1, 2, 3)
a = [1, 2]
b = 3

"""
It's also called grabbing excess items. The original feature is grabbing excess
parameters in function definitions with *args, e.g.
"""


def f(*args):
    pass


"""
On the other hand, the star parameter is not only used to grab items, but
also for unpacking in the reversed situation, e.g. in function calls:
"""
t = (1, 2, 3)
f(*t)

"""
And also, newly, in sequence literals.
"""
x = [1, 2, 3, 4, 5]
a, b, c, *d = (*x,)
t = [*range(1, 11)]
