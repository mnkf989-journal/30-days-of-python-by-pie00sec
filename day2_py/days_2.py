# ============================================
# DÍA 2: 30 DÍAS DE PROGRAMACIÓN EN PYTHON
# ============================================

# ---------- NIVEL 1: DECLARACIÓN DE VARIABLES ----------

# Variables de tipo string (texto)
nombre = "Luis Angel"
apellido = "Murillo Yanez"
# ¡OJO! Aquí le faltaba un espacio entre nombre y apellido
full_name = nombre + " " + apellido  # "Luis Angel Murillo Yanez"
pais = "Mexico"
ciudad = "Tijuana"

# Variables de tipo numérico
edad = 20          # Entero (int)
anio = 2026        # Entero (int)

# Variables de tipo booleano (True/False)
# ¡OJO! input() devuelve string, no booleano
is_married = False   # Correcto: valor booleano
is_true = True       # Correcto: valor booleano
is_light_on = False  # ¡Esta me faltó declarar!

# Múltiples variables en una línea
nombre2, apellido2, pais2 = "maria", "jose", "mexico"

# ---------- NIVEL 2: FUNCIONES Y OPERACIONES ----------

# 1. Verificar tipos de datos con type()
print("\n=== TIPOS DE VARIABLES ===")
print(f"nombre: {type(nombre)}")
print(f"apellido: {type(apellido)}")
print(f"edad: {type(edad)}")
print(f"is_married: {type(is_married)}")

# 2. Longitud con len()
print(f"\nLongitud del nombre: {len(nombre)}")
print(f"Longitud del apellido: {len(apellido)}")

# 3. Comparación de longitudes
if len(nombre) > len(apellido):
    print("El nombre es más largo")
elif len(nombre) < len(apellido):
    print("El apellido es más largo")
else:
    print("Tienen la misma longitud")

# 4. Operaciones aritméticas
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
producto = num_one * num_two
division = num_one / num_two
modulo = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two  # ¡Esta me faltó!

print(f"\nOperaciones:")
print(f"5 + 4 = {total}")
print(f"5 - 4 = {diff}")
print(f"5 * 4 = {producto}")
print(f"5 / 4 = {division}")
print(f"5 % 4 = {modulo}")
print(f"5 ** 4 = {exp}")
print(f"5 // 4 = {floor_division}")

# 5. Círculo
from math import pi

radio = 30
area = pi * (radio ** 2)
circum = 2 * pi * radio  # ¡Esta me faltó!

print(f"\nCírculo de radio 30m:")
print(f"Área: {area:.2f} m²")
print(f"Circunferencia: {circum:.2f} m")

# ¡OJO! Aquí usé radio2 en lugar de radio
radio2 = float(input("Ingresa el radio del círculo: "))
area2 = pi * (radio2 ** 2)  # Ahora sí uso radio2
print(f"Área con radio {radio2}m: {area2:.2f} m²")

# 6. Datos del usuario con input()
print("\n=== INGRESA TUS DATOS ===")
nombre_user = input("Nombre: ")
apellido_user = input("Apellido: ")
pais_user = input("País: ")
edad_user = int(input("Edad: "))

print(f"\nHola {nombre_user} {apellido_user} de {pais_user}, tienes {edad_user} años")

# 7. Palabras reservadas de Python
# help('keywords')  # Descomenta para verlas