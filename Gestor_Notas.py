cursos = ["Matematica Discreta", "Algoritmos", "Contabilidad", "Algebra lineal", "Precalculo"]
notas = [80, 61, 77, 83, 60]

def Registro_Curso():
    # pedir el nombre del curso
    nombre = input("Ingrese el nombre del nuevo curso:\n ").strip()

    # si el nombre está vacío
    if not nombre:
        print("El nombre no debe estar vacío.\n")
        return  # salir de la función, try intenta ejecutar el codigo

    # pedir la nota del curso
    try:
        nota = float(input("Ingrese la nota obtenida en ese curso:\n "))
    except ValueError:#si falla, #ValueError que es ocurre cuando el tipo de dato es correcto, pero el valor no tiene sentido para la operación.
        print("La nota debe ser un número.\n")
        return

    # validar rango de la nota
    if nota < 0 or nota > 100:
        print("La nota no está en el rango de 0 a 100.\n")
        return

    # guardar el curso y nota
    cursos.append(nombre)
    notas.append(nota)
    print(f"Curso '{nombre}' con nota {nota} registrado correctamente.\n")
    

#Mostrar cursos y notas previamente registrados
def Mostrar_cursos_notas():
    # si no hay cursos
    #Zip combina ambas listas, enumerate(..., start=1) le asigna un valos a cada dato desde 1
    #for i, en cada fila toma 1 curso y un nombre
    if not cursos:
        print("No hay cursos ni notas para mostrar\n")
        return
    #  si hay cursos, mostrarlos
    else:
       print("\nCursos y notas registrados:")
       for i in range(len(cursos)): #len contar la cantidad de elementos que tiene una lista, enera un ciclo desde 0 hasta el tamaño de la lista menos 1
           print(f"{i+1}. {cursos[i]} - Nota: {notas[i]}")
           

#calcular promedio
def Calcular_promedio():
     if not notas:
        print("No hay notas para calcular el promedio.\n")
        return
     else:
         promedio = sum(notas) / len(notas)  # Suma todas las notas y divide entre el total de elementos len
         print("El promedio General es:", promedio)

def Aprobados_Reprobados():
    #si la lista está vacía,retornara un mensaje
    if not notas:
        print("No hay notas registradas.\n")
        return
    #Se crean dos variables para llevar la cuenta de cuantos reprobados y reprobados
    aprobados = 0
    reprobados = 0
    #Toma cada elemento de la lista notas uno por uno, nota por nota
    for nota in notas:
        #si la nota nota es mayor o igual que 60
        if nota >= 60:
            aprobados += 1
        #si no
        else:
            reprobados += 1
    
    print(f"Cursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}\n")

#Buscar curso por nombre
def Buscar_curso():
    if not cursos:
        print("No hay cursos registrados.\n")
        return
    
    nombre = input("Ingrese el nombre (o parte) del curso a buscar: ").strip().lower() #.lower convierte todo a minúsculas
    #Si encuentra cursos que coincidan con la búsqueda, los guardará aquí
    encontrados = []
    #recorre la lista obteniendo el índice i y el nombre del curso.
    for i, curso in enumerate(cursos):
        if nombre in curso.lower():  # coincidencia parcial, se buscan semenjanzas en la escritura
            #se guarda el resultado cuando encuentra un curso que coincide con lo que escribió,
            encontrados.append((curso, notas[i]))
    #notas[i] sirve para enlazar la nota que corresponde al curso con el mismo índice.
    #la lista tiene elementos encontrados.
    if encontrados:
        print("Cursos encontrados:")
        for curso, nota in encontrados:
            print(f"- {curso} =  Nota: {nota}")
        print()
        #Si está vacía
    else:
        print("No se encontró ningún curso con ese nombre.\n")

def mostrar_menu():
    print("====== GESTOR DE NOTAS ACADÉMICAS ======")
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (búsqueda lineal:")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota (ordenamiento burbuja)")
    print("9. Ordenar cursos por nombre (ordenamiento inserción)")
    print("10. Buscar curso por nombre (búsqueda binaria)")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios (pila)")
    print("13. Salir")
    print("=====================================")
    
# Bucle principal del menú
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        Registro_Curso()
    elif opcion == "2":
        Mostrar_cursos_notas()
    elif opcion == "3":
        Calcular_promedio()
    elif opcion == "4":
        Aprobados_Reprobados()
    elif opcion == "5":
        Buscar_curso()
    elif opcion == "6":
        print("Función de actualizar nota aún no implementada.\n")
    elif opcion == "7":
        print("Función de eliminar curso aún no implementada.\n")
    elif opcion == "8":
        print("Función de ordenar cursos por nota aún no implementada.\n")
    elif opcion == "9":
        print("Función de ordenar cursos por nombre aún no implementada.\n")
    elif opcion == "10":
        print("Función de búsqueda binaria aún no implementada.\n")
    elif opcion == "11":
        print("Función de simulación de cola aún no implementada.\n")
    elif opcion == "12":
        print("Función de historial con pila aún no implementada.\n")
    elif opcion == "13":
        print("Saliendo del programa... ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.\n")



   






       




