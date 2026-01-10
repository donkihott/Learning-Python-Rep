x = 2
y = 5
tmp = x
x = y
y = tmp
del tmp
print('x_temp! = ', x)
print('y_temp = ', y)
# This script swaps the values of x and y and prints them.
# The expected output is:
# x_temp = 5
# y_temp = 2

# Swapping using a temporary variable
tmp1 = x
tmp2 = y
x = tmp2
y = tmp1
del tmp1, tmp2
print('x_tmp2 = ', x)
print('y_tmp1 = ', y)
# x_tmp2 = 2
# y_tmp1 = 5

# Swapping using tuple unpacking
tmp1, tmp2 = x, y
x, y = tmp2, tmp1
del tmp1, tmp2
print('x_tmp,tmp = ', x)
print('y_tmp,tmp = ', y)
# x_tmp,tmp = 5
# y_tmp,tmp = 2

# Swapping using arithmetic operations
A = x, y
y, x = A
print('x_A = ', x)
print('y_A = ', y)
print(type(A))
# x_A = 2
# y_A = 5
# <class 'tuple'>

x, y = y, x
print('x = ', x)
print('y = ', y)
# x = 5
# y = 2

a = 1
b = 2
c = 3
a, b, c = c, a, b + c
print('a = ', a)
print('b = ', b)
print('c = ', c)
# a = 3
# b = 1
# c = 5


