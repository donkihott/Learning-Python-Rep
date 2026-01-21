
def hello_n(name:str, n:int):
    for i in range(n):
        print('привет', name)

hello_n('Вася', 5)
hello_n('Петя', 3)
vasya = 'Вася', 3
hello_n(*vasya)
##########################################################
############   range(start, stop, step)

A = range(1, 6) # stop = 1 dont write
print(*A) # 1 2 3 4 5
A = [1, 2, 3]
print(type(A)) # <class 'list'>
A = [(1, 10), (2, 20), (3, 30)]




