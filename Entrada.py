# Entrada.py
# Autor: Brayan Javier Ruiz Navarro
# Fecha de Creación: 15/09/2019

entrada=input()
print(type(entrada))
# La variable booleana contiene el resultado de verificar si lo capturado es digito
# y si no se encuentra un punto en lo capturado, lo que indicaria que se trata de un numero con decimales.
# Si find retorna -1 quiere decir que lo buscado en este caso un punto decimal no se encontro.
esEntero=(entrada.isdigit() and entrada.find (".")==-1)
if (esEntero):
    print("Dato entero")
else:
    print("Dato no es entero")