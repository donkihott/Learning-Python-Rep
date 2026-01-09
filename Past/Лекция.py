x = 2
y = 5
print('x =', x, 'y =', y)

temp = x  # 2
x = y  # 5 (x=5 y = 5)
y = temp  # 2
print('x =', x, 'y =', y)

tmp1 = y
tmp2 = x
x = tmp1
y = tmp2
print('x =', x, 'y =', y)

tmp1, tmp2 = y, x
x, y = tmp1, tmp2
print('x =', x, 'y =', y, 'tmp1, tmp2 = y, x')

A = y, x
x, y = A
print('x =', x, 'y =', y, 'A = y, x | x, y = A')

x, y = y, x
print('x =', x, 'y =', y, 'x, y = y, x')

a = 1
b = 2
c = 3
a, b, c = b, c, a + b
print(a, b, c)

s = 'ABC\nEFG\t000'
print(s)

s1 = 'ABC'
x, y, z = s1
print('x =', x, 'y =', y, 'z =', z)

s2 = 'ABCDEFG'
x, y, z, *rest = s2
print('x =', x, 'y =', y, 'z =', z, 'rest =', rest)

for x in rest:
    print(x)

for x in s2:
    print(x)

A = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(type(A))
for x in A:
    print(x)
B = A
A[0] = 1000  # change А, but was changed A and В

C = A.copy()
print("A == C", A == C)
A[1] = 2000  # the result same that - B[1] = 2000
A[-1] = 999     # Add last think in the list
print('id B', id(B))
print('id C', id(C))
print('id A', id(A))

A = [1, 2, 3, 4, 5]
B = list(range(3, 0, -1))
X = A + B
print(X,'A + B')

print('A is B', A is B)
print('A is C', A is C)
print('A == C', A == C)
print('A ', A)
print('B ', B)
print('C ', C)


