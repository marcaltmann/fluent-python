values = [
    ('hello', 5),
    (5, 5),
    ('hello', 'hello'),
    ('left', 1, 2, 3, 4, 5, 6, 'right'),
]

for value in values:
    match value:
        case [str(a), int(b)]:
            print(f'String/Int combination: {a}, {b}')
        case [int(a), int(b)]:
            print(f'Int/Int combination: {a}, {b}')
        case [str(a), str(b)]:
            print(f'String/String combination: {a}, {b}')
        case ['left', *_, 'right']:
            print('Bingo')
