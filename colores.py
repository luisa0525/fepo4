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
