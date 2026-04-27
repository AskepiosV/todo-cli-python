tasks = []

def nuevaTarea(tasks):
    print('1. Agregar 2. Ver 3. Eliminar')
    eleccion = int(input("Que deseas hacer: "))

    if eleccion == 1:
        tasks.append(input("Describa la tarea nueva: "))
    else:
        print("error")


