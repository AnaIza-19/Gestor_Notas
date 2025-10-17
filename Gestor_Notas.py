# ------------------------- "Gestor Notas Académicas"-------------------------

# Listas globales que almacenan los cursos, sus notas y el historial de cambios realizados en todo el sistema.
notas = []
cursos =[]
historial_cambios = [] #Variable que simula una Pila en el sistema.

#----------------------------------------------------------------------------
# 1.                 "REGISTRO Y VISUALIZACION DE LAS NOTAS" 
#----------------------------------------------------------------------------

#                     "1. Funcion: Registro curso"

# Permite registrar un nuevo curso con su nota correspondiente.

def Registro_Curso():
#PRE: El usuario debe ingresar un nombre de curso no vacío.
# La nota ingresada debe ser un número entre 0 y 100.

#POST:Se agrega un nuevo curso y su nota a las listas globales,(notas, cursos).
# Se registra el cambio en la pila de historial.(Historial de cambios)
    nombre = input("Ingrese el nombre del nuevo curso:\n ").strip()
    nota = 0
    if not nombre:
        print("El nombre no debe estar vacío.\n")
        return  
    try:
        nota = float(input("Ingrese la nota obtenida en ese curso:\n "))
    except ValueError:#si falla
        print("La nota debe ser un número.\n")
        return
    if nota < 0 or nota > 100:# validar rango de la nota
        print("La nota no está en el rango de 0 a 100.\n")
        return
    else:
        cursos.append(nombre)
        notas.append(nota)
        print(f"Curso '{nombre}' con nota {nota} registrado correctamente.\n")
        input("Presione enter para continuar")    
     

#        "2. Opcion Mostrar cursos y notas previamente registrados"

# Muestra todos los cursos y notas registrados.

def Mostrar_cursos_notas():
#PRE : Debe haber al menos un curso registrado, en el sistema.
#POST : Se imprime en pantalla la lista completa de cursos y notas.

    if not cursos:#No hay cursos
        print("No hay cursos ni notas para mostrar\n")
        return 
     
    else: #  si hay cursos, mostrarlos   
       print("\nCursos y notas registrados:")
       for i in range(len(cursos)): 
           print(f"{i+1}. {cursos [i]} - Nota: {notas [i]}") 
       input("Presione enter para continuar")

#----------------------------------------------------------------------------
# 2.                "CÁLCULOS Y ESTADÍSTICAS DE LOS DATOS"
#----------------------------------------------------------------------------

#                      "3. Funcion : calcular promedio"

# Calcula el promedio general de las notas.

def Calcular_promedio():
#PRE:Debe haber al menos una nota en la lista, notas.
#POST: Muestra el promedio calculado con dos decimales, en la consola principal.
     if not notas:#no hay cursos
        print("No hay notas para calcular el promedio.\n")
        return
     promedio = 0 #Variable para el promedio
     promedio = sum(notas) / len(notas)  
     print(f"El promedio General es:{promedio:.2f}")
     input("Presione enter para continuar")


#            "4. Funcion: Contar Cursos Aprobados y Reprobados"

# Cuenta los cursos aprobados y reprobados.

def Aprobados_Reprobados():
#PRE:  Deben existir notas registradas.
# Cuenta los cursos aprobados (>=60) y reprobados (<60)
#POST: Se imprime la cantidad de cursos aprobados y reprobados.
    if not notas:
        print("No hay notas registradas.\n")
        return
   #Variables nuevas para almacenar los reprobados y aprobados
    aprobados = 0
    reprobados = 0

    for nota in notas: 
        if nota >= 60:
            aprobados += 1
        else:
            reprobados += 1
    
    print(f"Cursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}\n")
    input("Presione enter para continuar")

#----------------------------------------------------------------------------
#  3.           "BÚSQUEDA Y ACTUALIZACIÓN DE LAS NOTAS Y CURSOS"
#----------------------------------------------------------------------------

#                   "5. Funcion: Buscar curso por nombre"

#  Busca un curso por nombre o parte del nombre (búsqueda lineal).

def Buscar_curso():
#PRE:Deben existir cursos registrados.
#POST: Muestra los cursos encontrados que coincidan parcial o totalmente.
    
    if not cursos:# No hay registros
        print("No hay cursos registrados.\n")
        return
    
    nombre = input("Ingrese el nombre (o parte) del curso a buscar: ").strip().lower() #.lower convierte todo a minúsculas
    #Si encuentra cursos que coincidan con la búsqueda, los guardará aquí
    encontrados = []
    
    #Compara la entrada con los datos que estan registrados
    for i, curso in enumerate(cursos):
        if nombre in curso.lower():  
            encontrados.append((curso, notas[i]))
    
    if encontrados:
        print("Cursos encontrados:")
        for curso, nota in encontrados:
            print(f"- {curso} =  Nota: {nota}")
        print()
        
    else:#Si está vacía
        print("No se encontró ningún curso con ese nombre.\n")
        
    input("Presione enter para continuar")


#                "6. Funcion: Actualizar nota de un curso"

# Actualiza la nota de un curso ya existente.

def Actualizar_Nota_De_Cursos():
     
#PRE: Debe existir al menos un curso registrado. El curso ingresado debe existir en la lista.
#Modifica la nota de un curso existente.

#POST:Actualiza la nota del curso seleccionado.
# Registra el cambio en el historial.
     if not cursos:
        print("No hay cursos registrados para actualizar su nota.\n")
        return
#Muestra los cursos que se encuentran en el sistema
     print("Cursos Disponibles en el Sistema:")
     for curso in cursos:
        print(f"- {curso}")
     Nombre = input("Ingrese el nombre del curso que desea cambiar su nota: ").strip()
     cursos_lower = [c.lower() for c in cursos]
     # Verificar si el curso existe
     if Nombre.lower() in cursos_lower:
        
        indice = cursos_lower.index(Nombre.lower())
        try:
         #pedir la nueva nota
            nueva_nota = float(input(f"Ingrese la nueva nota para {cursos[indice]}: "))
            if 0 <= nueva_nota <= 100:
                nota_anterior = notas[indice]
                notas[indice] = nueva_nota
                print(f"Nota actualizada para el curso {cursos[indice]}.")
                historial_cambios.append(
                f"Se actualizó: {cursos[indice]} - Nota anterior: {nota_anterior} → Nueva nota: {nueva_nota}"
                )
            else:
                print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Por favor, ingrese un número válido para la nota.")
     else:
        print(f"El curso '{Nombre}' no se encuentra registrado aun en el Sistema.")
     input("Presione enter para continuar")


#                       "7. Funcion: Eliminar un Curso"

# Elimina un curso del sistema.

def Eliminar_Curso():
    # PRE: Debe existir al menos un curso registrado.
    # POST: El curso y su nota se eliminan solo si el usuario confirma.
    #       Se registra el cambio en el historial.

    if not cursos:
        print("No hay cursos registrados para eliminar.\n")
        return
    
    Eliminar = input("Ingrese el nombre del curso a eliminar: ").strip()
    cursos_lower = [c.lower() for c in cursos]
    
    if Eliminar.lower() in cursos_lower:
        indice = cursos_lower.index(Eliminar.lower())
        curso_eliminado = cursos[indice]
        nota_eliminada = notas[indice]

        # Solicitar confirmación al usuario
        confirmacion = input(f"¿Está seguro que desea eliminar '{curso_eliminado}'? (s/n): ").strip().lower()
        if confirmacion == "s":
            cursos.pop(indice)
            notas.pop(indice)
            print("Curso eliminado correctamente.\n")

            # Registrar el cambio en el historial
            historial_cambios.append(f"Se eliminó: {curso_eliminado} - Nota: {nota_eliminada}")
        else:
            print("Operación cancelada. El curso no fue eliminado.\n")
    else:
        print(f"El curso '{Eliminar}' no se encuentra registrado.\n")
       

#----------------------------------------------------------------------------
#  4.                    "ORDENAMIENTO Y BÚSQUEDA BINARIA"
#----------------------------------------------------------------------------

#          " 8. Funcion:  Ordenar cursos por nota (Ordenamineto Burbuja)"

# Ordena los cursos según sus notas (mayor a menor) usando el método de burbuja.

def ordenar_cursos_por_nota(cursos, notas):
#PRE: Debe haber cursos y notas registrados, en las listas globales, notas y Cursos
#POST:Las listas se reordenan y se muestran de mayor a menor nota, en la pantalla principal.
    if not cursos:
        print("No hay cursos registrados para ordenar.\n")
        return
    n = len(notas)
    for i in range(n):
        for j in range(0, n - i - 1): 
            if notas[j] < notas[j + 1]:
                #Intercambiar ambos notas
                notas[j], notas[j + 1] = notas[j + 1], notas[j]
                #Intercambiar cursos
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]
    
    print("Cursos ordenados por nota (descendente):")
    for i in range(n):
        print(f"{i+1}. {cursos[i]} - Nota: {notas[i]}")
      


#     "9. Funcion: Ordenar cursos por nombre. (Ordenamineto de insercion)"

# Ordena los cursos alfabéticamente usando el método de inserción.

def ordenar_cursos_por_nombre(cursos, notas):
#PRE:Debe haber cursos y notas registrados.
#POST: Los cursos quedan ordenados alfabéticamente junto con sus notas.
    if not cursos:
        print("No hay cursos registrados para buscar.\n")
        return
    n = len(cursos)
    for i in range(1, n):
 #Se guardan temporalmente el curso y la nota que se van a insertar en la posición correcta.
        curso_actual = cursos[i]
        nota_actual = notas[i]
        j = i - 1
        # Mover los cursos mayores que curso_actual una posición adelante
        while j >= 0 and cursos[j].lower() > curso_actual.lower():
            #Se mueve el curso y la nota en la posición j una posición a la derecha
            cursos[j + 1] = cursos[j]
            notas[j + 1] = notas[j]
            j -= 1
        cursos[j + 1] = curso_actual
        notas[j + 1] = nota_actual
    print("Cursos ordenados por nombre:")
    for i in range(n):
        print(f"{i+1}. {cursos[i]} - Nota: {notas[i]}")
    input("Presione enter para continuar")


#             "10. Funcion: Buscar curso por nombre (búsqueda binaria)"

# Busca un curso usando búsqueda binaria (se requiere la lista este ordenada). 

def buscar_curso_binario(cursos, notas):
#PRE:Deben existir cursos registrados.
#La lista debe estar ordenada alfabéticamente.
#POST: Muestra el curso encontrado o nos muestra si no existe

    # Ordenar cursos alfabéticamente y sincronizar notas
    if not cursos:
        print("No hay cursos registrados para buscar.\n")
        return
    #combina cada curso con su nota en pares, unidas.
    cursos, notas = zip(*sorted(zip(cursos, notas), key=lambda x: x[0].lower()))
    cursos = list(cursos)
    notas = list(notas)

    
    nombre_buscar = input("Ingrese el nombre del curso a buscar: ").strip().lower()

    #min y max son los índices de los extremos de la lista.
    min = 0
    max = len(cursos) - 1
    # Bucle de búsqueda binaria
    while min <= max:
        #Variable medio para  el índice de la posición central.
        medio = (min + max) // 2
        #nombre del curso en esa posición, convertido a minúsculas.
        curso_medio = cursos[medio].lower()
        if curso_medio == nombre_buscar:
            print(f"Curso encontrado: {cursos[medio]} - Nota: {notas[medio]}")
            return medio
        elif curso_medio < nombre_buscar:
            min = medio + 1
        else:
            max = medio - 1

    print("Curso no encontrado.")
    return -1
#----------------------------------------------------------------------------
# 5.                "ESTRUCTURAS DE LOS DATOS (PILA/COLA)""
#----------------------------------------------------------------------------

#         "11. Funcion: Simular una cola de solicitudes de revisión"

# Simula una cola (FIFO) de solicitudes de revisión.

def simular_cola_revision():
#PRE:Debe haber cursos registrados.
#POST: Ordena los cursos en orden de llegada (primero en entrar, primero en salir)
    if not cursos:
        print("No hay cursos registrados en el sistema\n")
        return
    cola = []  # lista vacía que funcionará como cola

    print("Ingrese curso para revisión (escriba 'fin' para terminar):")
    while True:
        curso = input("> ").strip()
        if curso.lower() == "fin":
            break
        cola.append(curso)  # se agrega al final de la cola

    print("\nProcesando solicitudes:")
    while cola:  # mientras haya elementos en la cola
        curso = cola.pop(0)  # Extrae el primero en entrar
        print(f"Revisando: {curso}")
    input("Presione enter para continuar")


#           "12. Funcion : Mostrar historial de cambios (pila)"

#  Muestra el historial de cambios realizados (estructura tipo pila).

def Historial_de_cambios():
#PRE:Puede estar vacío (en ese caso no mostrará nada).
#POST:Se imprimen los cambios más recientes primero.
    if not historial_cambios:
        print("No hay cambios registrados.\n")
        return
    
    print("Historial de cambios recientes:")
    for i, cambio in enumerate(reversed(historial_cambios), 1):  # reversed = último primero
        print(f"{i}. {cambio}")
    input("Presione enter para continuar")

#----------------------------------------------------------------------------
# 6.                 "MENÚ PRINCIPAL DEL GESTOR DE NOTAS"
#----------------------------------------------------------------------------

def mostrar_menu():
    print("====== GESTOR DE NOTAS ACADÉMICAS ======")
    print("1. Registrar Cursos")
    print("2. Mostrar cursos")
    print("3. Calcular promedio")
    print("4. Contar Cursos Aprobados/Reprobados")
    print("5. Buscar Curso por nombre")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota (ordenamiento burbuja)")
    print("9. Ordenar cursos por nombre (ordenamiento inserción)")
    print("10. Buscar curso por nombre (búsqueda binaria)")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios (pila)")
    print("13. Salir")
  
#----------------------------------------------------------------------------
#  7.                         "PROGRAMA PRINCIPAL"
#----------------------------------------------------------------------------

while True:
    mostrar_menu()
    # Estructura de control que ejecuta cada función según la opción elegida
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        Registro_Curso()
    elif opcion =="2":
        Mostrar_cursos_notas()
    elif opcion == "3":
        Calcular_promedio()
    elif opcion == "4":
        Aprobados_Reprobados()
    elif opcion == "5":
        Buscar_curso()
    elif opcion == "6":
        Actualizar_Nota_De_Cursos()
    elif opcion == "7":
        Eliminar_Curso()
    elif opcion == "8":
        ordenar_cursos_por_nota(cursos, notas)
    elif opcion == "9":
        ordenar_cursos_por_nombre(cursos, notas)
    elif opcion == "10":
        buscar_curso_binario(cursos, notas)
    elif opcion == "11":
        simular_cola_revision()
    elif opcion == "12":
        Historial_de_cambios()
    elif opcion == "13":
        input("\nGracias por usar el Gestor de Notas Académicas. ¡Hasta pronto!\n")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
        



   






       




