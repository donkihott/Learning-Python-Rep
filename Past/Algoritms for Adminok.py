x = 15 / 4  # assign the name "x" to the expression "5/4" (3.75)
print(x)
type(x)  # What is the type of 'y'. Now it is class 'float' (3.75).

print('Change type x to class int')
x = int(x)  # Change type 'x' to class 'int'
print(x)  # (3)

x = 15 / 4
x = float(x)  # If str is float, it will not correct to change str to 'int'
print(x)  # (3.75)

print('round(3.75)')
a = round(3.75)
print(a)  # (4)

print('function into the str')
print(f'Привет, {a}!')  # (Привет, 4!) - 'f' before the ' and function in {} - Create function into the str

# branching into 4 options
x = 1
y = -1
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
else:  # when you did not take into account the option
    print("Никогда")