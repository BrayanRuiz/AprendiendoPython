# Multiplo.py
# Autor: Brayan Javier Ruiz Navarro
# Fecha de Creación: 15/09/2019

numero=int(input("Dame un numero: "))

# Si el residuo es cero quiere decir que el numero dado si es multiplo.
Multiplo3=((numero%3)==0)
Multiplo5=((numero%5)==0)
Multiplo7=((numero%7)==0)

# Aqui se evalua si el numero coincide con la instruccion anterior y si no coincide lo manda a else.
if ((Multiplo3 and Multiplo5) or Multiplo7):
    print("Muy bien")
else:
    print("Esta mal")