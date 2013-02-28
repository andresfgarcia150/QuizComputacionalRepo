# --------------- Universidad de los Andes ---------------
# ---------------   Fisica computacional   ---------------
# Tarea 2 - 2013 I
# Autor:
#       Andres Felipe Garcia Albarracin - 201012816

# Librerias
import sys

# Funciones
def letraValida(var):
    if var == ",": return False
    elif var == ";": return False
    elif var == ".": return False
    elif var == " ": return False
    elif var == "\n": return False
    elif var == "\r": return False
    elif var == "\xa0": return False
    elif var == "\xad": return False
    elif var == ":": return False
    elif var == "'": return False
    elif var == '"': return False    
    elif var == "(": return False
    elif var == ")": return False
    elif var == "[": return False
    elif var == "]": return False
    elif var == "{": return False
    elif var == "}": return False
    elif var == "<": return False
    elif var == ">": return False
    else: return True


# Tomar los archivos de entrada
a = len(sys.argv)

if (a != 2):
    print "Revise los parametros de entrada"
    sys.exit(1)

nombreArchivo = sys.argv[1]

# Vectores usados en el algoritmo
vectorCaracteres = []
vectorRepeticiones = []

# Leer el archivo dado por parametro
archivo = open(nombreArchivo,'r')

#totalCaracteres = len(archivo.read())
while 1:
    var = archivo.read(1)
    existe = 0          # Para determinar si la letra ya existe en vectorCaracteres
    if var == "":
        break           # En caso de que se termine de leer el archivo
    if (letraValida(var)):
        for i in range(len(vectorCaracteres)):
            if var == vectorCaracteres[i]:
                existe = 1
                vectorRepeticiones[i] = vectorRepeticiones[i] + 1
        if (existe == 0):
            vectorCaracteres = vectorCaracteres + [var]
            vectorRepeticiones = vectorRepeticiones + [1]

if (len(vectorCaracteres) != len(vectorRepeticiones)):
    print "ERROR los vectores no son identicos"
    sys.exit(1)

# Organizacion de los vectores
# Organizacion por medio del algoritmo de seleccion
listaRecorrido = range(len(vectorCaracteres))
for i in range(len(vectorCaracteres)-1):
    posMayor = i
    cantidadMayor = vectorRepeticiones[i]
    letraMayor = vectorCaracteres[i]
    for j in listaRecorrido[i:]:
        if (vectorRepeticiones[j] > cantidadMayor):
            cantidadMayor = vectorRepeticiones[j]
            letraMayor = vectorCaracteres[j]
            posMayor = j
    vectorCaracteres[posMayor] = vectorCaracteres[i]
    vectorRepeticiones[posMayor] = vectorRepeticiones[i]
    vectorCaracteres[i] = letraMayor
    vectorRepeticiones[i] = cantidadMayor

# Calculo del procentaje
numeroCaracteres = len(vectorCaracteres)
totalCaracteres = sum(vectorRepeticiones)
vectorPorcentajes = range(len(vectorCaracteres))
for i in listaRecorrido:
    vectorPorcentajes[i] = float(vectorRepeticiones[i])/totalCaracteres*100

# Creacion del archivo de salida
nombreArchivoSalida = "frecuencias_" + nombreArchivo
archivoSalida = open(nombreArchivoSalida,'w')
listaRecorrido = range(len(vectorCaracteres))
for i in listaRecorrido:
    lineaTexto = '%s      %.5f %s\n' % (vectorCaracteres[i], vectorPorcentajes[i], chr(0x25))
    archivoSalida.write(lineaTexto)
archivoSalida.close()

# Creacion del archivo con comentarios
nombreArchivoComentario = "comentario.txt"
archivoComentario = open(nombreArchivoComentario,'w')
lineaTexto = "Comentarios sobre la lectura del texto:" + nombreArchivo + "\n\n"
archivoComentario.write(lineaTexto)
archivoComentario.write("Los siguientes caracteres no se reconocen como validos: \n")
archivoComentario.write(" ;  .  ' '  \ n  \ r  \ xa0  \ xad  :  '  (  )  [  ]  {  }  <  >\n")
archivoComentario.write("Los siguientes caracteres fueron encontrados:\n")
for i in listaRecorrido:
    lineaTexto = vectorCaracteres[i] + ", "
    archivoComentario.write(lineaTexto)
lineaTexto = "\n\nEl numero de caracteres distintos encontrados en el texto es:  %d" % (numeroCaracteres)
archivoComentario.write(lineaTexto)
archivoComentario.close()

print "El numero de caracteres es: ", numeroCaracteres

# Calculo de la regresion
listaRecorrido = range(len(vectorCaracteres))
x = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0]

y = vectorPorcentajes	
y1 = y[0:20]

import numpy as np
import math

x2 = np.array(x)
y2 = np.array(y1)

z = np.polyfit(np.log(x2), np.log(y2), 1)
print "Los elementos de la regresion del libro ", nombreArchivo,  " son: \n", z, "\n"

