import random
import json

trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

sueldos = {}

def asignar_sueldos():
    for trabajador in trabajadores:
        sueldos[trabajador] = random.randint(300000, 2500000)
    print("Sueldos asignados aleatoriamente.")

def clasificar_sueldos():
    clasificacion = {
        "Bajos": [],
        "Medios": [],
        "Altos": []
    }
    for trabajador, sueldo in sueldos.items():
        if sueldo < 1000000:
            clasificacion["Bajos"].append((trabajador, sueldo))
        elif 1000000 <= sueldo < 2000000:
            clasificacion["Medios"].append((trabajador, sueldo))
        else:
            clasificacion["Altos"].append((trabajador, sueldo))
    
    for categoria, lista in clasificacion.items():
        print(f"{categoria}:")
        for trabajador, sueldo in lista:
            print(f"  {trabajador}: ${sueldo}")
    
def ver_estadisticas():
    if not sueldos:
        print("No se han asignado sueldos.")
        return
    
    sueldos_lista = list(sueldos.values())
    total = sum(sueldos_lista)
    max_sueldo = max(sueldos_lista)
    min_sueldo = min(sueldos_lista)
    promedio = total / len(sueldos_lista)
    
    print(f"Total de sueldos: ${total}")
    print(f"Sueldo máximo: ${max_sueldo}")
    print(f"Sueldo mínimo: ${min_sueldo}")
    print(f"Sueldo promedio: ${promedio:.2f}")

def reporte_sueldos():
    if not sueldos:
        print("No se han asignado sueldos.")
        return
    
    for trabajador, sueldo in sueldos.items():
        print(f"{trabajador}: ${sueldo}")

def mostrar_menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            asignar_sueldos()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()


