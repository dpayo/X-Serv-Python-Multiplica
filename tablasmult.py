#!/usr/bin/python
#Programa en python que calcula la tabla de multiplicar.

tabla=int(raw_input("Introduzca el numero de la  tabla que quiere: "))
rango=range(1,11);
if tabla <0 :
    print("Introduce una tabla mayor de 0 ")
else:
    print("Tabla de multiplicar de "+str(tabla)+"\n")
    for numerador in rango:
        print(str(tabla)+" X "+str(numerador)+ " = "+str(tabla*numerador)+"\n")
