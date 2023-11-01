#comentario de prueba
#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
#git remote add origin https://github.com/luisa0525/Colores.git
import random
import numpy as np
# cómo crear una lista
'''
lista = [1]
lista2 = [2]

#lista de listas

Listas = []

#print(Listas)

#Listas = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
#np.array(Listas).reshape(8,8)

#crear números aleatorios
for x in range(3):
    Listas.append(random.randint(1,256))
    #np.array(Listas).reshape(2,2)
print(Listas) # tenemos un cuadrito

ListaGrande = []
for l in range(64):
    ListaGrande.append(Listas.append(random.randint(1,256))) #tratamos de hacer los 8x8
    np.array(ListaGrande).reshape(8,8)
print(ListaGrande)
#print(x)  

#np.array(L).reshape(4,3)


'''
matriz=[]
for _ in range(8):
    fila=[]
    miscolores=[]
    for _ in range(8):
        numero=random.randint(0,255)
        miscolores.append(numero)
        fila.append(miscolores)
    matriz.append(fila)
print(matriz)
for i in range(8):
    print(matriz[i])
    
    
    

#como mostrar un solo punto de un solo color



#      clase de 11-01--2023

#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
#git remote add origin https://github.com/luisa0525/fepo4.git
a,b = 0,1

while a<10:
    print(a)
    a,b = b,a+b
    
    
def sumar(a,b):
    c = a+b
    return c
print(sumar(3,8))

def sumarTres(a):
    x=a+3
    return x
y=sumarTres(7)+2
print(y)


x=int(input())
y= int(input())
z=x+y
print(z)

'''
funcion1()

x=int(input())
y= int(input())
return x+y
'''


def sumar(a,b):
    return a+b

