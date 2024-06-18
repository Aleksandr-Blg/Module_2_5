# *args - распаковка запаковка позиционных параметров, которые содержат один элемент (списки, кортежи, множества)
# **kwargs - распаковка запаковка именованных параметров (словари)
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]

def data_structure(*args):
    sum = 0
    for i in args:
        if isinstance(i, int):
            sum += int(i)
        return
        print(Type(i))






