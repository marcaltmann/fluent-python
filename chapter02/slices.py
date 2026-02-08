"""
Some interesting things about slices, although I almost never
use them.

Interesting: The article about the syntax.
https://fpy.li/2-32

Also interesting: The slice object, e.g.:
"""

a = [*range(10)]
s = slice(2, 4)
a[s]

"""
I don't know how useful the other slice stuff is for me.
- The step/stride
- The negative stride
- Assigning to slices...

- Maybe the del operator, e.g.
"""
del a[1:2]

"""
The Ellipsis object (...) is also interesting, but cannot be
really used without NumPy multidimensional arrays etc.
"""
