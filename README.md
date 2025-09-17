# GestorNotas
Descripción del problema y requisitos
# Gestor de Notas Académicas
# Descripción del problema y requisitos
Este Gestor es  un sistema interactivo que permitira al estudiante llevar el control de las calificaciones obtenidas en sus cursos. Estara  diseñado para facilitar el registro, administración, modificación y análisis de notas de manera ordenada, sencilla y practica. La idea principal es que el estudiante pueda evaluar su rendimiento académico, por medio de un menú en una consola que le permita administrar sus calificaciones, donde podrá seleccionar varias opciónes dependiendo de loq ue desee verificar, hasta que desee salir del menú.

# A quien va dirigido
Este programa va  dirigido principalmente a estudiantes de nivel medio o universitario que desean tener un seguimiento personalizado de sus cursos y calificaciones. El sistema "Gestor de Notas Academicas" cubre varias necesidades de los estudiantes como la organización de su información académica, cálculo de  su promedio de notas, búsqueda de calificaciones específicas y eliminación de registros que ya no son necesarios.

# Requisistos del Sistema
# Funcionales
El sistema contara con algunas las siguientes opciones:

1. **Registrar un nuevo curso**  
   El usuario podrá ingresar el nombre del curso y la nota obtenida para almacenarla en el sistema, la nota debe ser 0 y 100.
   
3. **Mostrar todos los cursos y  las notas registradas**  
   Se desplegará una lista con los cursos y sus respectivas calificaciones.
   
5. **Calcular el promedio general**  
   Se calculará y mostrará el promedio de todas las calificaciones almacenadas, verificara primero si hay notas almacenadas.
   
4.**Contar cursos aprobados y reprobados**
Verificara si  la nota >= 60 los cursos estan aprobado sino resprobados.
Desplegara la lista con los cursos aprobados y reprobados.

7. **Buscar curso por nombre (búsqueda lineal)**
   Pedira al usuario ingresar el nombre del curso, lo buscara en toda la base del sistema, si esta, dara la informacion sobre ese curso, la nota y nombre.
   
# No funcionales  
1. Se ejecutara en una consola por medio del lenguaje de programacion Python.
2. No requerira el uso de librerias externas.
3. Utilizara distintas bucles, repetitos y normales en el lenguaje de pseudocodigo, del mismo modo utilizara conceptos de listas, pilas, colas, búsqueda lineal y binaria, y algoritmos de ordenamiento.
   
# Diseño del menú principal en pseudocódigo
El sistema utiliza las siguientes instrucciones en pseudocódigo:

- **INICIO y FIN**  
  Indican el comienzo y final del programa.

- **LEER**  
  Se utiliza para capturar entradas del usuario como el nombre del curso o la nota.

- **IMPRIMIR**  
  Muestra el menú principal y los resultados al estudiante. Ejemplo de opciones:

Mostrara a la pantalla principal, un menú con distintas opciones.
1. Registrar nuevo curso
2. Mostrar todos los cursos y notas
3. Calcular promedio general
4. Contar cursos aprobados y reprobados
5. Buscar curso por nombre (búsqueda lineal)
6. Actualizar nota de un curso
7. Eliminar un curso
8. Ordenar cursos por nota (ordenamiento burbuja)
9. Ordenar cursos por nombre (ordenamiento inserción)
10. Buscar curso por nombre (búsqueda binaria)
11. Simular cola de solicitudes de revisión
12. Mostrar historial de cambios (pila)
13. Salir
Seleccione una opción:
En conclusion IMPRIMIR lo usamos para enviar información a la pantalla principal, y para enviar resultados sobre las opciones.

**Bucle repetitivo (MIENTRAS … HACER … FIN_MIENTRAS)**
Lo emplearemos para que el menú principal deba mostrarse una y otra vez hasta que el estudiante elija la opción “13 Salir”, solo asi concluiremos el Bucle repetitivo.

**Condicionales para cada opción (SI … ENTONCES … SINO … FIN_SI)**
Controlan qué acción ejecutar según la opción ingresada, en el menú principal
1. SI opción == 1 ENTONCES
   1.1 <registrar nuevo curso>
1.2. SINO SI opción == 2 ENTONCES
    1.2.1 <mostrar todos los cursos y notas>.
   Codigo en Pyton
   Se crearon 2 listas para almacenar la informacion, del estudiante. cursos[] y Notas[]
   Funcion numero 1 para registrar un nuevo cursos
   Def Registro_Curso() : Pedir al usuario el nuevo curso, y nota creamos una variable para almacenar los datos, en el programa
   Usamos If para verificar que el curso no quede vacio. Implementamos otra condicion con Si(IF)
   La nota debe estar en una rango mayor de 0 y menor de 100.
   Usamos la funcion ,append para guardar el curso al final de la lista, mostrara un mensaje de el curso ya refistrado exitosamente.
   Creamos un menu para mostrar al usuario la funcion

   Implementacion de funcione de busqueda lineal, y binaria, creandon una nueva variable que almacene los elementos en minusculas para facilitar el cambio de forma descendente, y de forma alfabeticamente. Usando el bucle While y if. Por si no se encontraron elementos en las lista.
