def data_structure(*args):
    summ = 0
    for i in args:
        if isinstance(i, (int, float)):
            summ += i
        elif isinstance(i, str):
            summ += len(i)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]




data_structure(print(sum *args))
