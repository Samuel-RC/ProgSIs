import random


print(random.random())
print('ss')
print(random.uniform(2.5, 10))
print(random.randrange(10))
print(random.randrange(0,104,2))
print(random.randint(2,30))

tam = int (input('Dame un número positivo'))

lst1 = [1 if random.random()>.5 else 0 for i in range(tam)]
lst2 = [1 if random.random()>.5 else 0 for i in range(tam)]

lista1 = ['0', '1', '1', '1', '0']
lista2 = ['1', '0', '1', '0', '0']

k = random.randrange(tam)
lst3 = lst1[0:k] +lst2[k:tam]

tam1 = sum(lst3)
tam2 = sum(lst2)

if(tam1 > tam2):
    print('lista 1 es mayor que lista 2', list(lst1))
else:
    print('Lista 2 es mayor que lista 1', list(lst2))



