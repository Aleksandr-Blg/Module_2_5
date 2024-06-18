def my_func():
    return 'HELLO'
var1 = my_func()
print(var1)
###
def sum_func(num1, num2):
    return num1 + num2
var1 = sum_func(2, 5)
print(var1)
####

var1 = sum_func(5, num2=5, num3=1)
print(var1)
###
def sum_func(*args):
    return num_1 + num_2 + num_3
var_list = [1, 2, 3]
var1 = sum_func(5, 5, 1, 2, 5)
print(var1)