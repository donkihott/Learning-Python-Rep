import turtle
turtle.shape('turtle')
turtle.color('black')
turtle.shapesize(1)
turtle.speed(3)
# turtle.shape('arrow', 'circle', 'triangle', 'classic')
# turtle.width(5)
#
# turtle.backward(200)




            ### Упражнение №2: буква S
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)

        ### Упражнение №4: окружность
# a = 100
# for step in range(a):
#     turtle.forward(10)
#     turtle.left(360 / a)

#!!!!!!!!!!!!!!!!!!! Упражнение №5: больше квадратов!!!!!!!!!!!!!!!!!!!!!! 5) more cubs
# i = 50
# for x in range(-10, -110, -10):
#     turtle.penup()
#     turtle.goto(x * 2.5, x * 2.5) # change coordinats every cicle
#     turtle.pendown()
#     i = i + 50
#     for step in range(4):
#         turtle.forward(i) # bigger forward about 50 every new cub
#         turtle.left(90)


# Упражнение №6: паук
# i = 8
# w = 200
# for step in range(i):
#     turtle.right(360 / i)
#     turtle.forward(w)
#     turtle.stamp()
#     turtle.right(180)
#     turtle.forward(w)
#     turtle.right(180)

# Упражнение №7: спираль
# x = 100
# for step in range(600):
#     x += 1
#     turtle.forward(1)
#     turtle.left(360 / x + 1)

############ Упражнение №8: квадратная «спираль»
# x = 10
# for step in range(100):
#     x += 5
#     turtle.forward(x + 10)
#     turtle.left(90)

####################### Упражнение №9: правильные многоугольники ######################################
# x = 25
# n = 2
# f = 20

# def polygon():
#     for step in range(n):
#         turtle.forward(x)
#         turtle.left(360 / n)
#
# turtle.penup()
# turtle.forward(f)
# turtle.left((360 - 180 /(n + 1)) / 2)
# for step in range(10):
#     n += 1
#     x += 20
#     turtle.pendown()
#     polygon()
#     turtle.penup()
#     turtle.right((360 - (180 * (n - 2)) / n) / 2)
#     turtle.forward(f)
#     turtle.left((360 - (180 * (n - 1)) / (n + 1)) / 2)
#     turtle.pendown()
#
# s = 180 * (n - 2)
# print((360 - s / n) / 2) # corner right of triangle
# print((360 - (180 * (n - 1)) / (n + 1)) / 2) # corner right of cub

######################################

#    Упражнение №10: «цветок»
# n = 50
# def vertical_eight():
#     for step in range(n):
#         turtle.forward(10)
#         turtle.left(360 / n)
#     for step in range(n):
#         turtle.forward(10)
#         turtle.right(360 / n)
#
# for step in range(3):
#     vertical_eight()
#     turtle.right(360 / 3)

######################################

# Упражнение №11: «бабочка»
# n = 25
# def gorizontal_eight():
#     for step in range(n):
#         turtle.left(360 / n)
#         turtle.forward(10)
#     for step in range(n):
#         turtle.right(360 / n)
#         turtle.forward(10)
#
# turtle.left(90)
# for step in range(10):
#     n += 5
#     gorizontal_eight()

######################################

# Упражнение №12: пружина
# n = 25
# def horizontal_arc():
#     for step in range(n):
#
#         turtle.right(180 / n)
#         turtle.forward(10)
#
# def inverted_arc():
#     for step in range(n):
#         turtle.right(176 / n)
#         turtle.forward(2)
#
# turtle.left(90)
# for step in range(3):
#     horizontal_arc()
#     inverted_arc()

######################################

# Упражнение №13: смайлик
# a = 100
# def raund():
#     for step in range(a):
#         turtle.left(360 / a)
#         turtle.forward(10)
#
# def eye(a = 10):
#     for step in range(a):
#         turtle.left(360 / a)
#         turtle.forward(10)
#
# turtle.penup()
# turtle.forward(100)
# turtle.left(90)
# turtle.pendown()
# turtle.color('black', 'yellow')
# turtle.begin_fill()
# raund()
# turtle.end_fill()
#
# turtle.penup()
# turtle.goto(-100, 50)
# turtle.pendown()
# turtle.color('black', 'blue')
# turtle.begin_fill()
# eye()
# turtle.end_fill()
#
# turtle.penup()
# turtle.goto(10, 50)
# turtle.pendown()
# turtle.color('black', 'blue')
# turtle.begin_fill()
# eye()
# turtle.end_fill()
#
# turtle.penup()
# turtle.goto(-60, 30)
# turtle.right(180)
# turtle.color('black')
# turtle.width(10)
# turtle.pendown()
# turtle.forward(50)
#
# n = 150
# def inverted_arc():
#     for step in range(n):
#         turtle.right(180 / n)
#         turtle.forward(2)
#
# turtle.penup()
# turtle.goto(40, -50)
# turtle.color('red')
# turtle.width(15)
# turtle.pendown()
# inverted_arc()

######################################

# Упражнение №14: звезды

# n = 5
# x = (n - 2) / n * 180
# y = 180 - x
# a = 180 - 2 * y
#
# turtle.left(180)
# for step in range(n):
#     turtle.forward(100)
#     turtle.left(180 - a)
#
# print((n - 2)/n*180)
# print(180 - 2 * y)