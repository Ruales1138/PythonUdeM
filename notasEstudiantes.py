def obtener_calificaciones(num_estudiantes, num_asignaturas):
    matriz_calificaciones = []
    for i in range(num_estudiantes):
        print(f"\nIngresando calificaciones para el estudiante {i + 1}:")
        calificaciones_estudiante = []
        for j in range(num_asignaturas):
            while True:
                calificacion = float(input(f"Calificación para la asignatura {j + 1}: "))
                if 0 <= calificacion <= 5:
                    calificaciones_estudiante.append(calificacion)
                    break
                else:
                    print("Por favor, ingrese una calificación entre 0 y 5.")
        matriz_calificaciones.append(calificaciones_estudiante)
    return matriz_calificaciones

def calcular_promedios_estudiantes(matriz):
    promedios = []
    for calificaciones in matriz:
        suma = 0
        contador = 0
        for calificacion in calificaciones:
            suma += calificacion
            contador += 1
        promedio = suma / contador
        promedios.append(promedio)
    return promedios

def encontrar_mejores_peores(promedios):
    mejor_promedio = peor_promedio = promedios[0]
    mejor_estudiante = peor_estudiante = 1

    for i in range(1, len(promedios)):
        if promedios[i] > mejor_promedio:
            mejor_promedio = promedios[i]
            mejor_estudiante = i + 1
        if promedios[i] < peor_promedio:
            peor_promedio = promedios[i]
            peor_estudiante = i + 1
    
    return mejor_estudiante, mejor_promedio, peor_estudiante, peor_promedio

def calcular_promedios_materias(matriz, num_asignaturas):
    promedios_materias = []
    for j in range(num_asignaturas):
        suma = 0
        contador = 0
        for i in range(len(matriz)):
            suma += matriz[i][j]
            contador += 1
        promedio = suma / contador
        promedios_materias.append(promedio)
    return promedios_materias

def estudiantes_que_pierden(matriz, num_asignaturas):
    # Lista para guardar los estudiantes que pierden en cada asignatura
    estudiantes_pierden = []

    # Iteramos sobre cada asignatura
    for j in range(num_asignaturas):
        # Lista temporal para guardar los índices de los estudiantes que pierden en la asignatura j
        pierden_en_asignatura = []
        
        # Revisamos cada estudiante para la asignatura j
        for i in range(len(matriz)):
            if matriz[i][j] < 3:
                # Agregamos el estudiante a la lista (i + 1 para hacerlo más legible, empezando en 1)
                pierden_en_asignatura.append(i + 1)
        
        # Agregamos la lista de estudiantes que pierden en la asignatura j a la lista principal
        estudiantes_pierden.append(pierden_en_asignatura)

    return estudiantes_pierden

while True:
    num_estudiantes = int(input("Ingrese el número de estudiantes: "))
    num_asignaturas = int(input("Ingrese el número de asignaturas: "))
    if num_estudiantes > 0 and num_asignaturas > 0:
        break
    else:
        print("Por favor, ingrese valores positivos para el número de estudiantes y asignaturas.")

# Imprimir la matriz de calificaciones

matriz_calificaciones = obtener_calificaciones(num_estudiantes, num_asignaturas)
print("\nMatriz de calificaciones:")
for i in matriz_calificaciones:
    print(i)

# Encontrar al mejor y peor estudiante

promedios_estudiantes = calcular_promedios_estudiantes(matriz_calificaciones)
mejor_estudiante, mejor_promedio, peor_estudiante, peor_promedio = encontrar_mejores_peores(promedios_estudiantes)
print(f"\nEl estudiante {mejor_estudiante} tiene el mejor promedio: {mejor_promedio}")
print(f"El estudiante {peor_estudiante} tiene el peor promedio: {peor_promedio}")

# Promedios de materias

promedios_materias = calcular_promedios_materias(matriz_calificaciones, num_asignaturas)
print("\nPromedio de calificaciones por materia:")
i = 1
for promedio in promedios_materias:
    print(f"Materia {i}: {promedio}")
    i += 1

# Estudiantes que pierden cada materia

estudiantes_pierden = estudiantes_que_pierden(matriz_calificaciones, num_asignaturas)
print("\nEstudiantes que pierden cada materia:")
for j, estudiantes in enumerate(estudiantes_pierden, start=1):
    if estudiantes:
        estudiantes_str = ", ".join(map(str, estudiantes))
        print(f"Materia {j}: Estudiantes {estudiantes_str}")
    else:
        print(f"Materia {j}: Ningún estudiante perdió")