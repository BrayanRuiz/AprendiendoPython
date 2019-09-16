# Compara.py
# Autor: Brayan Javier Ruiz Navarro
# Fecha de Creación: 15/09/2019

numero1=int(input("Dame el numero uno: "))
numero2=int(input("Dame el numero dos: "))
salida="Numeros proporcionados: {} y {}. {}."
if (numero1==numero2):
    # Entra aqui si los numeros son iguales
    print(salida.format(numero1, numero2,"Los numeros son iguales"))
else:
    # Si los numeros NO son iguales
    if numero1>numero2:
        # Chequea si el primer numero es mayor al segundo.
        print(salida.format(numero1, numero2,"El mayor es el primero"))
    else:
        # Ahora si el numero mayor es el segundo
        print(salida.format(numero1, numero2,"El mayor es el segundo"))