# Tabla.py
# Autor: Brayan Javier Ruiz Navarro
# Fecha de Creación: 15/09/2019

numero=int(input("Dame un numero del 1 al 9: "))


for i in range(1,11):
    salida="{} x {} = {}"
    print(salida.format(numero,i,i*numero))
