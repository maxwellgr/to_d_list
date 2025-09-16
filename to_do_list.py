# to_do_list.py

def mostrar_menu():
    print("\n📋 MENÚ DE TAREAS")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Guardar y salir")

def cargar_tareas():
    try:
        with open("tareas.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    with open("tareas.txt", "w") as file:
        for tarea in tareas:
            file.write(tarea + "\n")

def ver_tareas(tareas):
    if not tareas:
        print("\n✅ No tienes tareas pendientes.")
    else:
        print("\nTus tareas:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def agregar_tarea(tareas):
    nueva = input("\nEscribe la nueva tarea: ")
    tareas.append(nueva)
    print("Tarea añadida ✅")

def eliminar_tarea(tareas):
    ver_tareas(tareas)
    if tareas:
        try:
            num = int(input("\nNúmero de la tarea a eliminar: "))
            if 1 <= num <= len(tareas):
                tarea = tareas.pop(num - 1)
                print(f"Tarea '{tarea}' eliminada ❌")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor escribe un número válido.")

def main():
    tareas = cargar_tareas()
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ")
        if opcion == "1":
            ver_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            guardar_tareas(tareas)
            print("Tareas guardadas. ¡Hasta luego! 👋")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()
