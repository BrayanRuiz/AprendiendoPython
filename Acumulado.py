# Acumulado.py
# Autor: Brayan Javier Ruiz Navarro
# Fecha de Creación: 15/09/2019

acumulado=int(0)
numero=str("")

while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
        print("Numero no capturado, Saliendo del programa...")
        break
    else:
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))