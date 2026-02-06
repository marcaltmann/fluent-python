"""
Operator '==' does some kind of deep equal.
How deep, I do not know.
So, a == b is True first, but after the append is False.

hash(a) fails, because it contains mutable objects.
hash(c) does not fail, it returns a (negative) number.
-> So c can be used a dict key.
"""

a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
b[-1].append(3)

c = (10, 'alpha')
