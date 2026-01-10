# - 'tuple' - Кортежи даних

x = 1
y = 2

y, x = 1, 2

x, y = y, x

T = 1, 2, 3, 4
print(type(T)) # <class 'tuple'>
print(T)
a, b, c, d = T
print(c) # 3

a = T[0]
print(a) # 1

a, b, * rest = T
print(a) # 1
print(b) # 2
print(rest) # [3, 4]

print(T) # (1, 2, 3, 4)
print(*T) # 1 2 3 4
print(*T, sep= ':') # 1:2:3:4
print(*T, sep= ':', end='!\n') # 1:2:3:4!  # \n - new line

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

##########################################################
############   множества и словари - неупорядоченные
############     set         dict
# if S = list
S = ['Moscow',
     'Dolgoprudny',
     'Piter']
S.append('Rostov') # to add in end / if you wont to find '', must to read all list
print(S) # ['Moscow', 'Dolgoprudny', 'Piter', 'Rostov']

# if S = set
S = {'Moscow',
     'Dolgoprudny',
     'Piter'}
S.add('Odessa') # put not to end
print(S) # {'Piter', 'Odessa', 'Moscow', 'Dolgoprudny'}
if 'Odessa' in S:
    print('Yes') # Yes - not need to read all set - find


for el in S:
    print(el) # print all set:
# Piter
# Dolgoprudny
# Odessa
# Moscow

####################### dict (ключ + значение)
D = {'Moscow' : 78621,
     'Dolgoprudny' : 6283,
     'Piter' : 82851}
D['Rostov'] = 762

for key in D:
    print(key, D[key]) # :
# Moscow 78621
# Dolgoprudny 6283
# Piter 82851
# Rostov 762

for key in D:
    print(key, sep= ',', end=',\n') # :

Plot = {}

Plot["ч. 1 ст. 51"] = "__ 2020 року о 00:00 годині, в м. Чорноморську Одеської області шляхом вчинив"

Plot['ст. 173'] = 'Фабула ст. 173'

Plot['ч. 1 ст. 173-2'] = "Фабула ч. 1  ст. 173-2"
Plot['ст. 48'] = 'Fabula ct 48'


for key in Plot:
    print(key)
A = list(key)
print(A)

