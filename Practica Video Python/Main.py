va1 = 8
print(type(va1))

va2 = 8.0
print(type(va2))

va3 = 2 + 3j
print(type(va3))

va1f = float(va1)
print(type(va1f))
print(type(va1))

v = True
f = False

print(v)
print(f)

print(type(v))
print(type(f))

msj = 'Holaaa'
print(type(msj))
print(msj)
print(msj[0])
#msj[0] = 'R' <- Linea que lanza el error#

#msj = 'Adioos'
print(type(msj))
print(msj)
print(msj[0])

print(len(msj))
print(msj[3:7])
print(msj[-5:-2])
msj2 = msj.strip()
print(msj2)
print(msj2.upper())
print(msj2.lower())
print(msj2.replace('o','a'))

print('aaa' in msj)

msj3 = msj + msj2
print(msj3)

print('*-*-*-*-*-*-*Cantidades*-*-*-*-*-*-*')

cantidad = 3
numero = 567
precio = 32.57

peticion = 'Quiero {} elementos del número {} que tienen precio de {}'
print(peticion)
print(peticion.format(cantidad,numero, precio))

print('*-*-*-*-*-*-*Listas*-*-*-*-*-*-*')
favorite_things = ['8',6 + 2.4j, True]
print(type(favorite_things))
print(type(favorite_things[0]))
print(type(favorite_things[1]))
print(type(favorite_things[2]))

print(favorite_things[-2])

dias = ['Lunes','Martes', 'Miercoles', 'Jueves','Viernes','Sabado','Domingo']
print(dias[-4:-1])
dias[3] = 'Juevessss'
print(dias)
dias.pop()
print(dias)
dias.pop(0)
print(dias)

dias.append('Domingo')
print(dias)

dias = ['Lunes'] + dias
print(dias)

lst1 = ['Lunes','Martes', 'Miercoles']
lst2 = ['Jueves','Viernes','Sabado']

lst1.extend(lst2)
print(lst1)

msj = 'Hola'
print(msj)
msj_list = list(msj)
print(msj_list)

lst1.remove('Miercoles')
print(lst1)

del lst1[0]
print(lst1)

lst1.clear()
print(lst1)

tupla = ('a', 'e', 'i', 'o', 'u')
print(type(tupla))
print(tupla)

print(tupla[2])

tupla1 = ('Lunes', 'Martes', 'Miercoles')
tupla2 = ('Jueves', 'Viernes', 'Sabado')
tupla3 = tupla1 + tupla2
print(tupla3)

repeticiones = tupla3.count('Lunes')
print(repeticiones)
lugar = tupla3.index('Viernes')
print(lugar)

diass = {'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado'}
print(type(diass))

print('Martes' in diass)

diass.remove('Jueves')
print(diass)

diass.add('Lunes')
print(diass)

conj ={'1','2','3'}
lst =['4','5']
conj.update(lst)
print(conj)

conj1 = {'Lunes','Martes'}
conj2 = {'Miercoles','Jueves'}

conj3 = conj1.union(conj2)
print(conj3)

muestra = conj1.pop()
print(muestra)
print(conj1)

conj1.clear()
print(conj1)

persona = {
    'Nombre' : 'Samuel',
    'Edad' : 21,
    'Estatura': 1.70,
}
print(persona)
print(persona['Nombre'])
print(persona['Edad'])
age = persona.get('Edad')
print(age)
persona['Estatura'] = 1.71
print(persona)

print('Edad' in persona)
print('Hobbies' in persona)

print(len(persona))
persona['Mascota'] = True
print(persona)

persona.pop('Edad')
print(persona)

persona.popitem()
print(persona)

del persona['Estatura']
print(persona)

persona.clear()
print(persona)
