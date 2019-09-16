# Aleatorio.py
# Autor: Brayan Javier Ruiz Navarro
# Fecha de Creación: 15/09/2019

# Python posee muchas librerias listas para usarse.
# A dichas librerias les da el nombre de modules (module)
# Para utilizar un modulo en un programa primero debe importarse, usando la instruccion import.
import random

# Se define la variable float, y se le asigna un valor.
numero1=float(10.5)

# En python, una funcion es un conjunto de instrucciones que procesan una tarea especifica
# Se declaran def, lo de la derecha forma parte de la funcion.
def NumeroAleatorio():
    #Se convierte a float el numero aleatorio generado por random.randrange()
    numero2=float(random.randrange(1,10))
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))

NumeroAleatorio()