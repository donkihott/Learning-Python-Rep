A = [1, 2, 3, 4]
for x in A:
    print('x[_]:', x)
# x[_]: 1
# x[_]: 2
# x[_]: 3
# x[_]: 4

A = "abcd"
for x in A:
    print('x"_":', x)
# x"_": a
# x"_": b
# x"_": c
# x"_": d

s = "ABC"
A = list(s)
for x in A:
    print('x(list): - ', x)
# x(list): -  A
# x(list): -  B
# x(list): -  C

for x in 1, 2, 3, 1:
    print('x(1,2,3,1):', x)
# x(1,2,3,1): 1
# x(1,2,3,1): 2
# x(1,2,3,1): 3
# x(1,2,3,1): 1
    print('x**2:', x**2)
# x**2: 1
# x**2: 4
# x**2: 9
# x**2: 1

for x in 1, 2, 3, 1:
    for y in 'a', 'b':
        print('x,y:', x, y)