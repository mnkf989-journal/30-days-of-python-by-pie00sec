# ============================================
# DÍA 3: 30 DÍAS DE PROGRAMACIÓN EN PYTHON
# ============================================

# NIVEL 1

age = 20
height = 1.73

num_com = 3+4j

# Calcular area del triangulo
print ("////Calcular el area de un triangulo/////")

base = float(input("Ingresa la base del triangulo: "))
altura =  float(input("Ingresa la altura del triangulo: "))
area = 0.5 * base * altura

print(f"El area resultante del triangulo es: {area}")

# Calcular el perimetro de un triangulo
print("///Ingrese los 3 lados del triangulo////")

lado_a = float(input("Ingresa el lado A: "))
lado_b = float(input("Ingresa el lado B: "))
lado_c = float(input("Ingresa el lado C: "))


perimetro = lado_a + lado_b + lado_c

print(f"El resultado del perimetro del triangulo es: {perimetro}")

# Calcular Area y perimetro de rectangulo
print("////Calcular el area y perimetro de rectangulo////")

largo = float(input("Ingresa el largo del rectangulo: "))

ancho = float(input("Ingresa el ancho del rectangulo: "))

perimetro2 = 2 * (largo + ancho)

print(f"El resultado del perimetro de un rectangulo es: {perimetro2}")

# Calcular el area y circuferencia de un circulo -- Aca utilizare la libreria Math para usar Pi (Eso lo aprendi ayer por mi propia cuenta)
from math import pi
print ("/////Calcular el area y circuferencia de un rectangulo////")
radio = float(input("Ingresa el radio del circulo: "))

area = pi * radio * radio

circuferencia = 2 * pi * radio

print(f"El resultado de area es: {area} El resultado de circuferencia es: {circuferencia}")

# Nivel 2

# Calcular pendiente e intersecciones de una recta

pendiente = 2
x = 0
interseccion_y = 2 * x - 2 
interseccion_x = 2 / 2  

print("Ecuación: y = 2x - 2")
print(f"Pendiente: {pendiente}")
print(f"Intersección con Y (cuando x=0): {interseccion_y}")
print(f"Intersección con X (cuando y=0): {interseccion_x}")

# Calcular pendiente y distancia entre dos puntos 
print("////Calcular pendiente y distancia entre dos puntos////")
import math

pendiente2 = (10-2) / (2-6)

distancia = math.sqrt((2-2)**2 + (10-6)**2)

print(f"El resultado de la pendiente de y distancia:  Pendiente: {pendiente} Distancia: {distancia} ")

# Comparar pendientes Ejercicio 8 y 9

print(f"Comparacion de pendientes: {pendiente} es igual {pendiente2} ? --- Resultado de la comparacion: {pendiente == pendiente2}")

#Aca agregue en vez de que comparara si son iguales dijera si son diferentes por eso ocupare != (Esto lo hice nada mas por gusto)

print(f"Comparacion de pendientes: {pendiente} no es igual {pendiente2} ? --- Resultado de la comparacion: {pendiente != pendiente2}")

#Comparar longitudes de strings dragon y python y buscar una comparacion que de falso.

print("Comparar las longitudes de strings de Python y dragon (?)")
print(len("python") < len("dragon"))

#Usar operador And
(f"La palabra on esta en la palabra python (?): {"on" in "python"}")


print(f"La palabra on esta en la palabra dragon (?): {"on" in "dragon"}")

print(f"La palabra on esta en ambas palabras Python y dragon (?): {"on" in "python" and "on" in "dragon"}")

#Verificar  si "Jargon" esta en la frase

frase = "I hope this course is not full of jargon"

print(f"La palabra Jargon esta en la frase: {frase} esto es: {"jargon" in frase}")

#Verificar que No hay 'On' en ambas

print(f"la palabra 'on' no esta en la palabra 'python' y 'dragon': {"on" not in "python" and "on" not in "dragon"}")

# Convertir longitud de texto

print(f"La palabra 'Python tiene: '{len("python")}' letras")

print(f"Conversion del numero de letras de python a 'Float', 'string'")

print(f"Longitud a float: {float(len("python"))}")
print(f"Longitud a string: {str(str(len("python")))}")

# Calcular si un numero es par

num = int(input("Ingresa el numero a verificar: "))

if num % 2 == 0:
    print(f"{num} es un numero par")
else:
    print(f"{num} no es un numero par")

#comparar division de piso
num2 = 7 // 3

print(num2)

num3 = int(2.7)

print(f"Comparacion de '{num2}' y '{num3} son iguales (?): {num2==num3} ")

# Comparar tipos de datos 

num_2 = "10"
num_3 = 10

print(f"estas dos variables son iguales (?) '{type(num_2), num_2}' -- '{type(num_3), num_3}': {type(num_2) == type(num_3)}")

#Calcula salario semanal

horas = input("Ingresa las horas trabajadas: ")

tarifa = input("Ingresa la tarifa: ")

pago == horas * tarifa

print(f"Tu pago es de: {pago}")

#Calcular segundos de vida

num_anio = input("Ingresa el numero de anios vividos: ")

segundos = num_anio * 365 * 24 * 60 * 60

print(f"La cantidad de anios vividos a segundos es: {segundos}")

#mostrar tabla de numeros
for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")