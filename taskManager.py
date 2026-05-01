import json 

def cargarTareas():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardarTareas(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def mostrarMenu():
    print("--------------------------\n1.Agregar Tarea\n2.Ver Tareas\n3.Eliminar Tarea\n4.Completar Tareas\n5.Editar Tarea\n6.Salir\n--------------------------")

def agregarTarea(tasks):
    nueva = (input("Describa la nueva tarea: "))
    tasks.append({"tarea": nueva, "completada": False})
    print("Tarea agregada...")
    guardarTareas(tasks)

def completarTareas(tasks):
    listarTareas(tasks)
    completa = int(input("Que tarea desea completar: "))
    tasks[completa - 1]["completada"] = True
    guardarTareas(tasks)

def listarTareas(tasks):
    print("Sus tareas pendientes: ")
    for index, l in enumerate(tasks, start = 1):
        print(index, l["tarea"], "[✔]" if l["completada"] else "[]")

def borrarTareas(tasks):
    listarTareas(tasks)
    pregunta = int(input("Que tarea desea borrar: "))
    confirmacion = input("Seguro que desea borrar la tarea seleccionada S/N: " ).lower()
    if confirmacion == "s":
        try:
            tasks.pop(pregunta - 1)
            print("Tarea eliminada...")
        except ValueError:
            print("Debe indicar un indice...")
    elif confirmacion == "n":
        return
    else:
        print("Responda con S o N ")
    guardarTareas(tasks)

def editarTareas(tasks):
    listarTareas(tasks)
    cambio = int(input("Que tarea desea editar: "))
    confirmar = input("Seguro que desea editar la tarea S/N: ").lower()
    nuevoTexto = input("Cual sera la nueva tarea: ")
    if confirmar == "s":
        try:
            tasks[cambio - 1]["tarea"] = nuevoTexto
            print("Se edito correctamente...")
        except ValueError:
            print("Debe indicar un indice... ")
    elif confirmar == "n":
        return
    else: 
        print("Responda con S o N...")
    guardarTareas(tasks)

tasks = cargarTareas()

while True:
    try:
        mostrarMenu()
        opcion = int(input("Que desea hacer: "))
    
        if opcion == 1:
            agregarTarea(tasks)
        elif opcion == 2:
            listarTareas(tasks)
        elif opcion == 3:
            borrarTareas(tasks)
        elif opcion == 4:
            completarTareas(tasks)
        elif opcion == 5:
            editarTareas(tasks)
        elif opcion == 6:
            print("Hasta luego Askepios....")
            break
    except ValueError:
        print("Debe escribir un numero...")
        



