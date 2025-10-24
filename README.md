# GestorNotas
*¿Qué aprendí?
Durante el desarrollo del Gestor de Notas Académicas, pude aprender a no solo a aplicar los conceptos básicos de la programación que usualmente se usan en Python, sino también a pensar como ser capaz de diseñar soluciones cuando surgen distintos escenarios, que logren ser eficientes y útiles para el usuario final.

También comprendí la importancia que conlleva tener una planificación antes de programar un sistema, dividiendo el proyecto en funciones o módulos más pequeños y específicos, que me ayudaron a llevar un mejor orden no solo en la ejecución sino también en la estructura del código. Aprendí a trabajar con listas que me ayudaron con el  almacenamiento de grupos de datos, y a aplicar pilas (LIFO) y colas (FIFO) para simular procesos reales, como también el historial de cambios o la gestión de solicitudes, en el programas.

También pude conocer e implementar  los algoritmos de ordenamiento (burbuja e inserción) y búsqueda (binaria y lineal), entendiendo cómo elegir el método más adecuado según la necesidad del sistema, según su estructura, ya que unos son más eficientes que otros dependiendo los daros que estos trabajen, otro aprendizaje que logre entender y usar fue la validación de datos de entrada, si estos eran los correctos o no, algo fundamental para evitar errores comunes y asegurar que el programa funcione de forma correcta ante cualquier tipo de usuario.

Además, logre crear un sistema interactivo por consola, bastante amigable y con mensajes claros que guían al usuario. Este proyecto me ayudó bastante a mejorar mi capacidad de análisis, y la forma en que buscaba ideas o planteamientos, como lo haría, como solucionaría mis errores al escribir código y documentación técnica.

*¿Qué fue lo más desafiante de resolver?
Lo más desafiante para mí de este proyecto fue haber lograr la estructura correcta entre las diferentes funciones para que todas trabajaran bien todas juntos sin generar conflictos, o errores.
Por ejemplo, en las funciones de actualizar, eliminar y ordenar los cursos se debían mantener sincronizadas varias listas  como la de (cursos y notas) sin perder coherencia, lo que me hizo revisar varias veces la lógica interna de cada función y hacer múltiples cambios y pruebas pruebas, para que funcionara correctamente
También fue difícil implementar los algoritmos de ordenamiento y búsqueda, porque muchas veces no funcionaba por que trabajan de manera distinta cada uno.  La búsqueda binaria, en particular, exigía que la lista estuviera previamente ordenada, por lo que tuve que comprender bien cómo interactuaban los diferentes métodos entre sí, por ejemplo, en esa tuve que reorganizar los lista antes de poder ser evaluada por el algoritmo.
Fue desafiante el manejo que se tenía sobre los errores del usuario. Tuve que considerar muchos escenarios posibles que pudieran ocurrir como : notas fuera de rango, entradas vacías, nombres inexistentes, opciones inválidas, entre otros. Diseñar el sistema para que fuera tolerante a estos errores y, al mismo tiempo este sea , fácil de usar, fue un proceso de aprendizaje constante y tardado.
Crear un programa modular y documentado también fue un reto bastante importante. Aprendí a aplicar comentarios, etiquetas PRE y POST, y a estructurar el código de forma ordenada para facilitar su comprensión futura.

*¿Qué aprendí con este proyecto?
Si tuviera más tiempo para seguir mejorando mi proyecto, me gustaría implementar varias funcionalidades nuevas y optimizar su estructura interna.
En primer lugar, incorporaría una interfaz gráfica, que permitiría a los usuarios interactuar con botones, menús y cuadros de texto en lugar de escribir comandos en una consola. Esto haría que el sistema fuera más visual, más práctico y accesible para todo tipo de público.
También me gustaría añadir una base de datos, para que los cursos y notas se guarden de forma permanente y no solo temporalmente, permitiendo asi al usuario poder conservar su información incluso después de haber cerrar el programa. Esto haría al gestor más eficiente.
Finalmente, con más tiempo, trabajaría en la optimización del código, dividiendo el proyecto en módulos y clases, aplicando principios de Programación Orientada a Objetos (POO) para mejorar la escalabilidad, reutilización y mantenimiento del sistema, creando estructura y no tantos módulos. Estas mejoras harían que el Gestor de Notas Académicas sea un programa educativo mas practico y puesto para todo publico no importando la edad.



