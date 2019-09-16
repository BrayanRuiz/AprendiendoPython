# Conversiones.py
# Autor: Brayan Javier Ruiz Navarro
# Fecha de Creación: 15/09/2019

# Se declara una variable str con una cadena de digitos
numero= "1234"
# Se muestra el tipo que tiene la variable.
# No es un str es un dato type.
print(type(numero))
# Se convierte la cadena a su equivalencia int.
numero=int(numero)
# Se muestra como el tipo a cambiado aunque se usa la misma variable.
print(type(numero))
# Se declara una variable con meta sustitucion (posiciones donde iran valores proporcionados usando format.)
salida="El numero utilizado es {}"
# Se muestra el resultado. La meta sustitucion hara que donde esta {} se coloque el valor de numero.
print(salida.format(numero))