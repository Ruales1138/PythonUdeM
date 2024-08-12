def obtener_calificaciones(num_estudiantes, num_asignaturas):
    # Crear una matriz vacía
    matriz_calificaciones = []

    # Iterar sobre el número de estudiantes
    for i in range(num_estudiantes):
        print(f"\nIngresando calificaciones para el estudiante {i + 1}:")
        calificaciones_estudiante = []
        # Iterar sobre el número de asignaturas
        for j in range(num_asignaturas):
            while True:
                try:
                    # Solicitar la calificación al usuario
                    calificacion = float(input(f"Calificación para la asignatura {j + 1}: "))
                    if 0 <= calificacion <= 10:  # Asumimos una escala de 0 a 10
                        calificaciones_estudiante.append(calificacion)
                        break
                    else:
                        print("Por favor, ingrese una calificación entre 0 y 10.")
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")
        
        # Agregar las calificaciones del estudiante a la matriz
        matriz_calificaciones.append(calificaciones_estudiante)

    return matriz_calificaciones

def imprimir_matriz(matriz):
    print("\nMatriz de calificaciones:")
    for fila in matriz:
        print(fila)

def calcular_promedios_estudiantes(matriz):
    promedios = []
    for calificaciones in matriz:
        promedio = sum(calificaciones) / len(calificaciones)
        promedios.append(promedio)
    return promedios

def calcular_promedios_materias(matriz, num_asignaturas):
    promedios_materias = []
    for j in range(num_asignaturas):
        suma = sum(matriz[i][j] for i in range(len(matriz)))
        promedio = suma / len(matriz)
        promedios_materias.append(promedio)
    return promedios_materias

def encontrar_mejores_peores(promedios):
    mejor_promedio = max(promedios)
    peor_promedio = min(promedios)
    mejor_estudiante = promedios.index(mejor_promedio) + 1
    peor_estudiante = promedios.index(peor_promedio) + 1
    return mejor_estudiante, mejor_promedio, peor_estudiante, peor_promedio

def estudiantes_que_pierden(matriz, num_asignaturas):
    estudiantes_pierden = [[] for _ in range(num_asignaturas)]
    for i in range(len(matriz)):
        for j in range(num_asignaturas):
            if matriz[i][j] < 3:
                estudiantes_pierden[j].append(i + 1)
    return estudiantes_pierden

def main():
    while True:
        try:
            num_estudiantes = int(input("Ingrese el número de estudiantes: "))
            num_asignaturas = int(input("Ingrese el número de asignaturas: "))
            if num_estudiantes > 0 and num_asignaturas > 0:
                break
            else:
                print("Por favor, ingrese valores positivos para el número de estudiantes y asignaturas.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
    
    # Obtener la matriz de calificaciones
    matriz_calificaciones = obtener_calificaciones(num_estudiantes, num_asignaturas)
    
    # Imprimir la matriz de calificaciones
    imprimir_matriz(matriz_calificaciones)
    
    # Calcular los promedios de los estudiantes
    promedios_estudiantes = calcular_promedios_estudiantes(matriz_calificaciones)
    
    # Calcular los promedios de las materias
    promedios_materias = calcular_promedios_materias(matriz_calificaciones, num_asignaturas)
    
    # Encontrar al mejor y peor estudiante
    mejor_estudiante, mejor_promedio, peor_estudiante, peor_promedio = encontrar_mejores_peores(promedios_estudiantes)
    
    print(f"\nEl estudiante {mejor_estudiante} tiene el mejor promedio: {mejor_promedio:.2f}")
    print(f"El estudiante {peor_estudiante} tiene el peor promedio: {peor_promedio:.2f}")
    
    # Imprimir los promedios de cada materia
    print("\nPromedio de calificaciones por materia:")
    for i, promedio in enumerate(promedios_materias, start=1):
        print(f"Materia {i}: {promedio:.2f}")
    
    # Determinar y listar los estudiantes que pierden cada materia
    estudiantes_pierden = estudiantes_que_pierden(matriz_calificaciones, num_asignaturas)
    
    print("\nEstudiantes que pierden cada materia:")
    for j, estudiantes in enumerate(estudiantes_pierden, start=1):
        if estudiantes:
            estudiantes_str = ", ".join(map(str, estudiantes))
            print(f"Materia {j}: Estudiantes {estudiantes_str}")
        else:
            print(f"Materia {j}: Ningún estudiante perdió")

if __name__ == "__main__":
    main()
