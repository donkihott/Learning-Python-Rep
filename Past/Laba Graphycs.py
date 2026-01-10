# http://cs.mipt.ru/python/lessons/lab1.html
import numpy as np # Данная библиотека обеспечивает удобную работу с векторам.
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, x**2)
plt.show()

plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
plt.show()

x = np.arange(-10, 10.01, 0.01)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(x, np.sin(x), label=r'$f_1(x)=\sin(x)$') # Текстовые поля в matplotlib могут содержать разметку LaTeX,
plt.plot(x, np.cos(x), label=r'$f_2(x)=\cos(x)$')   # заключенную в знаки $. Буква r перед кавычками говорит python,
plt.plot(x, -x, label=r'$f_3(x)=-x$')               # что символ "\" следует оставить как есть и не интерпретировать
plt.xlabel(r'$x$', fontsize=14)                     # как начало спецсимвола (например, перевода строки - "\n").
plt.ylabel(r'$f(x)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)   # Или используя legend(), где можно указать место расположения подписей к кривым
plt.show()                              # на графике в параметре loc.

data = [33, 25, 20, 12, 10]
plt.figure(num=1, figsize=(6, 6))
plt.axes(aspect=1)
plt.title('Plot 3', size=14)
plt.pie(data, labels=('Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'))
plt.show()

