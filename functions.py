# Объявление функции
# Функции - именованный блок кода, который мы можем вызывать в разных участках нашей программы по имени
from operator import itemgetter
from pprint import pprint

from loops import users


def my_func():
    print("Мы вызвали функцию!")

my_func() #вызов функции

#--------------------------------------------------------------------------------------------

#Функция с позиционными аргументами, т.е. функция, в которую мы что-то передадим

def sum_numbers(a, b):
    print(a + b)

sum_numbers(10, 15)
sum_numbers(20, 30)
sum_numbers(-2334234234324234, 1)

#часто в функциях используется типизация, т.е. подскази у аргументов, например, аргументы только число
def sum_numbers(a: int, b: int):
    print(a + b)

sum_numbers(10, 15)
sum_numbers('a', 'b') #код НЕ УПАДЕТ, питон просто нам подскажет, что ожидает число. Эти аннотации что, чтобы предупредить, что хотели другие значения

#--------------------------------------------------------------------------------------------

#Функция с именованными аргументами
sum_numbers(a=5, b=10) #ранее были позиционные аргументы, т.е. они подтягивались в порядке очереди, а тут мы конкретно определяем
sum_numbers(b=5, a=10)

#--------------------------------------------------------------------------------------------

#Функция с аргументами по умолчанию
#именнованные аргументы очень часто используются в функциях, в которых есть какие-то значения по умолчанию
def multiply(n, mult: int =2):
    print(n * mult)
multiply(10) #указываем только n, т.к. инт указан по умолчанию
multiply(10, mult=5) #тут явно указываем, что mult=5


#--------------------------------------------------------------------------------------------

#Возвращаем значение

def sum2(a: int, b: int):
    return a+b #возвращаем сумму из этой функции, поэтому мы можем присвоить ее результат в переменную
    # на слове return функция прекратит свое выполнение.
    # т.е. мы вернем сумму из 2 элементов запишем ее в n = sum(10, 20)

n = sum2(10, 20)
print(n) # сначала запишем сумму, только потом принт, иначе сразу после return работать не будет

#--------------------------------------------------------------------------------------------
#пример аргументов по умолчанию в функции print
#def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
#где sep=' ' - это пробел между ааргументами в принте
#end='\n' - новая строка, чтобы каждый новый принт был с новой строки
#file=None - тут можем указать название файлов, вместо того, чтобы выводить на экран значение
print(1,2,3, sep=" | ")

#--------------------------------------------------------------------------------------------
#Возвращаем несколько значений
def return_tuple():
    return 1, 2, 3 #функция возвращает 3 элемента
    #что нужно сделать, чтобы получить эти 3 элемента? далее

t = return_tuple()
print(t) #вывод всех 3 элементов

t1, t2, t3 = return_tuple()
print(t1, t2, t3)

#мы не можем 3 значения положить в 2 переменные, будет ошибка
#t1, t2 = return_tuple()
#print(t1, t2)
#как можно обойти данную ошибку
t1, *t2 = return_tuple() #специальный оператор *. Получается так - 1ое значение в одну переменную, а все остальные в t2
# если *, это точно будет список, пример принта: 1 [2, 3]
print(t1, t2)

#игнорирование элементов, т.е. если возвращаются 3 элемента, но нам нужен 1
t1, _, _ = return_tuple() #указываем позиции, которые не нужны (подчсеркивание)
t1, *_ = return_tuple() #все не нужны, кроме 1 (подчсеркивание)
print(t1)
#--------------------------------------------------------------------------------------------
#Переменное количество аргументов на примере print
def custom_print(*args): #это значит, что в функцию можно передать много аргументов и они все будут в одной переменной
    for arg in args: #для каждого аргумента в списке аргументов
        print(arg) #мы использовали принт для каждого аргумета
custom_print(1,2,3,4,5)

#распаковка taple(объекта) (вместо возвращения одного элемента, множества)
def custom_print(*args):
    print(args) #выводит переменные как 1 аргумент
    print(*args) #распаковался в одельные 5 значений


#--------------------------------------------------------------------------------------------
#Переменное количество именованных аргументов
def custom_named_print(*args, **kwargs): #собирает только именованные аргументы
    print(args, kwargs) #вывод значений и словаря (1,2,3,4,5) {end="!n", sep = " | "}
    print(*args, **kwargs) #распаются в именованные аргументы этой функции, т.е. теперь не словаль, а как аргументю Теперь не положаться как то, что нужно распечатать, а как аргументы функции

custom_named_print(1,2,3,4,5, end='!\n', sep = " | ")

#--------------------------------------------------------------------------------------------
#Область видимости переменных

v = 123
#в данном примере v независимы друг от друга

def my_awesome_func():
    v = 456 #она никак не связана с переменной выше, НО если бы этой строчки не было, то бралась бы переменная выше
    print(v)

print(v) #123
my_awesome_func() #456
print(v) #123

#--------------------------------------------------------------------------------------------
#Функция тоже объект
#как строки, словари и т.п.

p = print #это значит, что функцию принт присловили к переменной p
#функцию можно использовать как переменную и это нормально

p(1,2,3,4,5)

users = [
    {"name":"Oleg", "age": 32},
    {"name":"Sergey", "age": 24},
    {"name":"Stanislav", "age": 15},
    {"name":"Olga", "age": 45},
    {"name":"Maria", "age": 18}
]

'''
#для сортировки словарей нужен признак, по которому мы будем сравнить
def get_age(user):
    #pprint(user)#тут просто список без сортировки выводится
    return user["age"] #мы сделали функцию, которая будет применяться для каждого элемента из этого списка и будет вытаскивать 1 из атрибутов

#Пример, где это может использоваться
#users.sort() #сортируем список. получается не ОК, т.к. это спиоск не обычных типов, а словарей, мы не сможем их просто сравнить

users.sort(key=get_age, reverse=True) #Читаем - отсортируюй пожалуйста пользователей по признаку из этой функции
pprint(users)
#reverse=True - сортировка в обратную сторону
'''
#Ананимная фукция, т.е. вызов функции, например, при сортировке
users.sort(key=lambda user: user['age']) #указывается аргумент и то значение, которое нужно вернуть, т.е. ту операцию, которую нужно сделать
pprint(users)
#lambda используется, когда нужно передать функцию, как аргумент куда-то дальше, например сортировка

#
users.sort(key=itemgetter("age")) #itemgetter - Это функция, которая вернет функцию
pprint(users)