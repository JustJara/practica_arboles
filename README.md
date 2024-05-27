# Práctica de árboles (Heap)

## Autores

- Felipe Villa Jaramillo
- Juan Pablo Cardona Bedoya

## ¿Qué es y para qué es?

Se desarrolla un programa de gestión y priorización de pacientes de una sala de urgencias.
Al llegar los pacientes se deben de evaluar y asignar el triaje acorde a la siguiente tabla:

     ------------------------------------------------------------------------------
    | NIVEL DE URGENCIA  | TIPO DE URGENCIA  |    COLOR     |  TIEMPO DE ESPERA   |
    -------------------------------------------------------------------------------
    |       1            |  RESUCITACION     |    ROJO      |  ATENCIÓN INMEDIATA |
    -------------------------------------------------------------------------------
    |       2            |  EMERGENCIA       |    NARANJA   |  10 - 15 MINUTOS    |
    -------------------------------------------------------------------------------
    |       3            |  URGENCIA         |   AMARILLO   |  60 MINUTOS         |
    -------------------------------------------------------------------------------
    |       4            |  URGENCIA MENOR   |   VERDE      |  2 HORAS            |
    -------------------------------------------------------------------------------
    |       5            |  SIN URGENCIA     |    AMARILLO  |  4 HORAS            |
    -------------------------------------------------------------------------------
## ¿Cómo se usa el programa?
- Para ejecutar el programa se debe entrar a la carpeta raíz del proyecto y ejecutar el siguiente comando por consola:
    - <pre> python3 app.py </pre>

## ¿Cómo está hecho?

El programa está hecho para el uso desde consola y no utiliza ninguna libreria externa.

La organización de los módulos es así:
 - Dentro de src tenemos lo siguiente:
   - console_view: Donde se encuentra la lógica que permite el uso de interfaz por medio de consola
   - model: Donde se encuentra las diferentes clases utilizadas en el programa las cuales son: Patient, Minheap y Queue.
 - Por último el archivo app.py contiene la lógica para que se ejecute el programa, es decir que desde allí se ejecuta para que toda la aplicación funcione correctamente.

## Requisitos que debía cumplir el programa

- Crea una clase llamada Paciente que tenga los siguientes atributos: Número Paciente (identificador único), Genero, Nombre, Edad, Triaje.
- Registrar (insertar) un paciente, debe ser posible agregar nuevos pacientes, el
registro debe conservar el orden de llegada y la prioridad, el triaje 1 debe quedar
en la raíz ó seguido de esta dependiendo del orden de llegada.
- Consultar paciente próximo a atención, sin eliminar de la cola de prioridad (solo
consulta)
- Opción atender siguiente, en esta opción se debe extraer el paciente que
continua en atención acorde a la prioridad y orden de llegada
- Consultar los pacientes que están en espera en general
- Consultar los pacientes que están en espera por triaje
- Opción eliminar paciente, el sistema debe dar la opción si un paciente se desea
retirar de la sala de urgencias, este debe ser eliminado, conservando la
prioridad de los restantes y el orden de llegada, la eliminación debe ser por
nombre y/o por Id.