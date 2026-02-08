import array

# These are list comprehensions, i.e. listcomps:
# Lists are container sequences.

l = [ord(x) for x in 'hello']

t_shirts = [(size, color) for size in ['S', 'M', 'L'] for color in ['Black', 'White']]


# These are generator expressions, i.e. genexps:
# Arrays are flat sequences.

t = tuple(ord(x) for x in 'hello')

a = array.array('I', (ord(x) for x in 'hello'))
