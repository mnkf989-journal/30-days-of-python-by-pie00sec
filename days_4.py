# Día 4: Strings

# 1. Concatenar 'Treinta', 'Días', 'De', 'Python'
treinta = 'Treinta'
dias = 'Días'
de = 'De'
python = 'Python'
espacio = ' '
treinta_dias_de_python = treinta + espacio + dias + espacio + de + espacio + python
print(treinta_dias_de_python)

# 2. Concatenar 'Codificación', 'Para', 'Todos'
codificacion = 'Codificación'
para = 'Para'
todos = 'Todos'
codificacion_para_todos = codificacion + espacio + para + espacio + todos
print(codificacion_para_todos)

# 3. Declarar variable empresa
empresa = "Codificación para todos"

# 4. Imprimir empresa
print(empresa)

# 5. Imprimir longitud de empresa
print(len(empresa))

# 6. Cambiar a mayúsculas
print(empresa.upper())

# 7. Cambiar a minúsculas
print(empresa.lower())

# 8. capitalize(), title(), swapcase()
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())

# 9. Cortar (rebanar) la primera palabra
primera_palabra = empresa.split()[0]
print(primera_palabra)

# 10. Verificar si contiene 'Codificación'
print("Codificación" in empresa)

# 11. Reemplazar 'Codificación' por 'Python'
print(empresa.replace("Codificación", "Python"))

# 12. Cambiar "Python for Everyone" a "Python for All"
python_for_everyone = "Python for Everyone"
print(python_for_everyone.replace("Everyone", "All"))

# 13. Dividir 'Codificación para todos' por espacio
print(empresa.split())

# 14. Dividir lista por coma
empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(empresas.split(", "))

# 15. Carácter en índice 0
print(empresa[0])

# 16. Último índice de la cadena
print(empresa[-1])

# 17. Carácter en índice 10
print(empresa[10])

# 18. Acrónimo para 'Python For Everyone'
pfe = "Python For Everyone"
acronimo_pfe = pfe[0] + pfe[7] + pfe[11]
print(acronimo_pfe)

# 19. Acrónimo para 'Codificación para todos'
cpt = "Codificación para todos"
acronimo_cpt = cpt[0] + cpt[12] + cpt[17]
print(acronimo_cpt)

# 20. Posición de primera 'C'
print(empresa.index('C'))

# 21. Posición de primera 'F'
print(empresa.index('F'))

# 22. Última posición de 'l' en "Codificación para todos"
texto_l = "Codificación para todos"
print(texto_l.rfind('l'))

# 23. Primera aparición de "porque"
oracion = "No se puede terminar una oración con porque porque porque es una conjunción"
print(oracion.index("porque"))

# 24. Última aparición de "porque"
print(oracion.rfind("porque"))

# 25. Cortar 'porque porque'
indice_porque = oracion.index("porque")
indice_ultimo_porque = oracion.rfind("porque")
print(oracion[indice_porque:indice_ultimo_porque + len("porque")])

# 26. Primera aparición de "porque" (repetido)
print(oracion.index("porque"))

# 27. Cortar 'porque porque' (repetido)
print(oracion[indice_porque:indice_ultimo_porque + len("porque")])

# 28. ¿Comienza con 'Codificación'?
print(empresa.startswith("Codificación"))

# 29. ¿Termina con 'Codificación'?
print(empresa.endswith("Codificación"))

# 30. Remover espacios
empresa_con_espacios = " Codificación para todos "
print(empresa_con_espacios.strip())

# 31. isidentifier()
print("30DaysOfPython".isidentifier())
print("treinta_días_de_python".isidentifier())

# 32. Unir lista con #
bibliotecas = ['Django', 'Flask', 'Botella', 'Pyramid', 'Falcon']
print(" # ".join(bibliotecas))

# 33. Nueva línea
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Tabulación
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 35. Formato de string (radius)
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# 36. Formato de operaciones
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")