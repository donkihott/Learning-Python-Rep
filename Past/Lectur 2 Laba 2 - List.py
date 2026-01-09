# from random import *
# import turtle

# Упражнение
# Нарисуйте при помощи случайных поворотов и перемещений картину броуновских движений.
# turtle.color('red')
# turtle.shape('turtle')
# turtle.speed(3)
# turtle.shapesize(1)
#
# for step in range(100):
#    turtle.forward(random() * 45)
#    if (random() * 45) % 2 == 0:
#        turtle.right(randint(0, 180))
#    else:
#        turtle.left(randint(0, 180))

# A = [1, 2, 3]
# B = [4, 5]
# C = A + B
# D = B * 3
# print(C) # [1, 2, 3, 4, 5]
# print(D) # [4, 5, 4, 5, 4, 5]
#
# for i in range(len(A)):
#    print(A[i])  # 1
#                 # 2
#                 # 3
# for elem in A:
#     print(elem, end = ' ') # 1 2 3
#
# A = ['red', 'green', 'blue']
# print(' '.join(A)) # red green blue
# print(''.join(A)) # redgreenblue
# print('***'.join(A)) # red***green***blue

############################# TEXT
with open('test.txt', 'r') as file:
    for line in file:
        print(line)
# 1 AAAAAAAAAAAA
#
# 2 BBBBBBBBBBB
#
# 3 CCCCCCCCCCCC
#
# 4 DDDDDDDDDDDDD

from random import randint
import turtle
number_of_turtles = 5
steps_of_time_number = 100

pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))

for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(2)