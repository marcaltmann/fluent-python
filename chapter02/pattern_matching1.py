"""
Introduced in Python 3.10.

Evidently taken from Elixir and making everything more complicated.
On the other hand, what is it useful for? Some parsing situations,
maybe XML parsing with deep nesting?
Or just checking if something, e.g. a JSON or XML document, has a
specific structure?
"""

commands = [
    ['ADD', 5],
    ['SUB', 1],
    ['DEL'],
    ['SHUTDOWN'],
]

for command in commands:
    match command:
        case ['ADD', value]:
            print(f'Adding {value}...')
        case ['SUB', value]:
            print(f'Subtracting {value}...')
        case ['DEL']:
            print('Deleting...')
        case _:
            raise SyntaxError('Pattern not valid.')
