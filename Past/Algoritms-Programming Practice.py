


print('formula choose all numbers from "start" (9) to (0) - "stop"')
x = 9  # start (9)
while x >= 0:  # choose all numbers from 'start' (9) to (0) - 'stop'
    print(x)
    x -= 1  # 'step', the came: x = x - 1

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


