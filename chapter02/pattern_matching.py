"""
Introduced in Python 3.10
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
