s = 'Hello World'
print("s('_') -", type(s)) # s('Hello World') <class 'str'>

s = "Hello World"
print('s("_") -', type(s)) # s("Hello World") <class 'str'>

s = """Hello World
I`m a multiline string
that spans multiple lines"""
print('s("""_""") -', type(s)) # s(s"""_""") - <class 'str'>        
print(s)
# Hello World
# I`m a multiline string
# that spans multiple lines

s = "Hello\nWorld\nI`m a multiline string\nthat spans multiple lines"
print('s("_\n_") -', type(s)) # s("_\n_") - <class 'str'>
print(s)
# Hello
# World
# I`m a multiline string...

s = r"Hello\I'm a raw string\That doesn't process escape sequences"
print("s(r'_\_') -", str(type(s))) # s(r'_\_') - <class 'str'>
print(s) # Hello\I'm a raw string\That doesn't process escape sequences

s = f'World'    # 'f' - ???????????????????????
print("s(f'_') -", str(type(s))) # s(f'_') - <class 'str'>

s = "ABC"
x, y, z = s
print('x = ', x) # x =  A
print('y = ', y) # y =  B
print('z = ', z) # z =  C

s = "ABCDEF..."
x, y, z, *rest = s
print('x =', x) # x = A
print('y =', y) # y = B
print('z =', z) # z = C
print('rest =', rest) # rest =  ['D', 'E', 'F', '.', '.', '.']
print(type(rest)) # <class 'list'>


# 'str' ??????????
s = 'ABC'
print(type(s))
t = r'tEF'
print("t(r'tEF') = " + str(type(t)))
f = f'FLKJF'
print("f(f'FLKJF') = " + str(type(f)))