"""
Adding and multiplying sequences are standard operations in Python.

The only practical application I can think of are formatting or
templates.
E.g. concatenating strings:
"""

a = 'Hello\n'
a += 'World.'
print(a)

"""
Also, I've used the mul operator for output formatting, e.g.
creating an str.format template string when I did not know the
exact number of '{}' parts.
It's also widely used for e.g. outputting 80 '-' characters when
printing a table or divider.
"""
print('-' * 80)

"""
The section also contains instructions for generating and inspecting
bytecode with the dis (disassembler) module:
>>> dis.dis('a = 1')
  0           RESUME                   0

  1           LOAD_CONST               0 (1)
              STORE_NAME               0 (a)
              RETURN_CONST             1 (None)

Don't know if this is helpful in the future.

Lastly, after pointing out a strange behaviour of the
augmented assignment operator (+=) when used with tuples,
Ramalho recommends not putting mutables objects into tuples.
"""
