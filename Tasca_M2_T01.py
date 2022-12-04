#Ejercicio 1
#Allison Garces Castaño

#---------------------------------------------------------------------------------------

#Meses del año por trimestres.

t1 = ["enero", "febrero", "marzo"]
t2 = ["abril", "mayo", "junio"]
t3 = ["julio", "agosto", "septiembre"]
t4 = ["octubre", "noviembre", "diciembre"]

mesesAño = [t1,t2,t3,t4]

print("Meses del año: ",mesesAño)


#Ejercicio 2

#---------------------------------------------------------------------------------------

#Segundo mes del primer trimestre

print("Segundo mes del primer trimestre: ",mesesAño[0][1])

#---------------------------------------------------------------------------------------

#Los meses del primer trimestre

print("Los meses del primer trimestre: ",mesesAño[0][:])

#---------------------------------------------------------------------------------------

#Septiembre y Octubre
print("Los meses 09 y 10:", mesesAño[2][2], mesesAño[3][0])

print("\n")

#--------------------------------------------------------------
#Ejercicio 3

import random

#---------------------------------------------------------------------------------------

#desordenados = random.sample(range(12), 11)
desordenados = [1,6,44,3,2,8,5,3,4,5,0,12,4,3,3]
print("lista de numeros desordenados: ", desordenados)

#---------------------------------------------------------------------------------------

#¿Cuántos números hay?
print("Cantidad de numeros: ",len(desordenados))

#---------------------------------------------------------------------------------------

#¿Cuántas veces aparece el número 3?
print("Repeticiones del numero 3 en la lista: ", desordenados.count(3))

#---------------------------------------------------------------------------------------

#¿Cuántas veces aparecen los números 3 y 4?
print("Repeticiones de los numeros 3 y 4 en la lista: ", desordenados.count(3),"= Veces repetido 3 y " ,desordenados.count(4),"= Veces repetido 4")

#---------------------------------------------------------------------------------------

#¿Cuál es el mayor número?
print("El numero mayor es: ",max(desordenados))

#---------------------------------------------------------------------------------------

#¿Cuáles son los 3 números más pequeños?

import heapq
print("Los 3 elementos mas pequeños: ",heapq.nsmallest(3, desordenados))

print("\n")

#---------------------------------------------------------------------------------------

#Ejercicio 4

import math

compra = { 
    "Pomes" : {
        "Qty": 5, 
        "€": 0.42
        }, 
    "Peres" : {
        "Qty": 3, 
        "€": 0.66
        } 
    }

print("Diccionario de Compra: ",compra)

#---------------------------------------------------------------------------------------

#Añade alguna fruta más
otra = {"maduixes":{"Qty":7, "€":0.99}}
compra.update(otra)

print("Nuevas frutas agregadas: ",compra)

#---------------------------------------------------------------------------------------

#¿Cuánto han costado las peras en total?

Peres = compra.get("Peres")

PeresCantidad = Peres.get("Qty")
PeresPrecio = Peres.get("€")

valorPeres = PeresPrecio * PeresCantidad

print("Las peras en total costaron: ", valorPeres)

#Otra solucion: print("Las peras han costado: ",math.prod(dict.values(compra["Peres"])))

#---------------------------------------------------------------------------------------

#¿Cuántas frutas hemos comprado en total?

print("Se han comprado",len(compra),"frutas en total")

#---------------------------------------------------------------------------------------

#¿Cuál es la fruta más cara?

valorInicial = 0
for frutas in compra:
    fruta = compra[frutas]
    frutaNombre = fruta.get("Qty")
    frutaValor = fruta.get("€")
    if frutaValor > valorInicial:
        frutaCara = frutas
        valorInicial = frutaValor
print("La fruta más cara es: ", frutaCara)


