# Lecture 1 "Programming Practice"
# https://www.youtube.com/watch?v=us7y0UhTq0s&list=PLRDzFCPr95fIDJUvFxvzWxg-V9BmZlMMe&index=3
s = 'Hello world!!!'
print(s)

print()
print('str * 3')
print(s * 3)

# if you click and select several lines with the mouse, then print it in all lines
print(5)
print(5)

# Ctrl + Alt + L - fixes all bugs
print()
print('"x" to the expression "5/4"')
x = 15 / 4  # assign the name "x" to the expression "5/4" (3.75)

y = x  # assign the name "y" to the expression "x"
print(y)

y == x  # are two names equal? The result is "True" or "False"

x is y  # Is "x" "y"? The result is "True" or "False"

y >= 3  # Comparison "y" is greater than or equal to "3"? The result is "True" or "False"

type(x)  # What is the type of 'y'. Now it is class 'float' (3.75).
print()
print('Change type x to class int')
x = int(x)  # Change type 'x' to class 'int'
print(x)  # (3)

s = '12345.99'
print()
print('Str into the foat. If str is float, it will not correct to change str to int')
x = float(s)  # If str is float, it will not correct to change str to 'int'
print(x)  # (12345.99)

print()
print('float to int - without everything after the "." (Not round)')
y = int(x)
print(y)  # (12345) - without everything after the '.' (Not round)

print()
print('round(12345.99)')
a = round(12345.99)
print(a)  # (12346)

# name = input() - The text from Keyboard

name = 'Yura'
print()
print('str and function across the "," ')
print('Привет', name, '!')  # (Привет Yura !)

print()
print('function into the str')
print(f'Привет, {name}!')  # (Привет, Yura!) - 'f' before the ' and function in {} - Create function into the str

# x = x - 1 is x -= 1
print()
print('formula choose all numbers from "start" (9) to (0) - "stop"')
x = 9  # start (9)
while x >= 0:  # choose all numbers from 'start' (9) to (0) - 'stop'
    print(x)
    x -= 1  # 'step'

print()
print(' cicle for choose numbers that were put')
# 'cicle {for}')
for x in 9, 8, 7, 6, 5, 4, 3, 2, 1:  # a lot of nambers
    print(x)

# range(start, stop, step)
print()
for i in range(20, 10, -2):
    print(i)

# 4 possible variants
# 1)
x = 1
y = -1
if y > 0:
    if x > 0:
        print(1)
    else:
        print(2)
else:
    if x < 0:
        print(3)
    else:
        print(4)

# 2)
if x > 0 and y > 0:
    print(1)
else:
    if x < 0 and y > 0:
        print(2)
    else:
        if x < 0 and y < 0:
            print(3)
        else:
            print(4)

# 3) with verification if you did not take into account the option
if x > 0 and y > 0:
    print(1)
else:
    if x < 0 and y > 0:
        print(2)
    else:
        if x < 0 and y < 0:
            print(3)
        else:
            if x > 0 and y < 0:
                print(4)
            else:  # when you did not take into account the option
                print("Никогда")
# 3) else + if = elif
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

import turtle
def david():
    for step in range(6):  # number of ways = 360 / number of degrees
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(100)
            turtle.left(360 / 3)
        turtle.end_fill()
        turtle.forward(100)
        turtle.right(360 / 6)  # () - number of degree of rotation

turtle.shape('turtle') # to look like 'turtle'
turtle.shapesize(5) # take size ()
turtle.color('green', 'yellow') # (color of pen, color of turtle and fell
turtle.pensize(3)
turtle.speed(10)

david()
turtle.backward(300)
david()

turtle.hideturtle()


