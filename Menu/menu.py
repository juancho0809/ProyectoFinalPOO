import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    
        print("""

Bienvenidos al Sistema de Distri Pizza

Escoja la opción de su preferencia:

1) Registrar Cliente

2) Actualizar Puntos

3) Reclamar Promocion 1

4) Reclamar Promocion 2

5) Reclamar Promoción 3
        """)
def opcion():       
    ciclo = 1
    while ciclo == 1:
        opcion = int(input("introduzca su tipo de pan favorito:"))

        if opcion == 1:
                    print("Registrar Cliente")
                    ciclo  = 2
        elif opcion == 2:
                    print("Actualizar Puntos")
                    ciclo  = 2
        elif opcion == 3:
                    print("Reclamar Pormoción 1")
                    ciclo  = 2
        elif opcion == 4:
                    print("Reclamar Pormoción 2")
                    ciclo  = 2
        elif opcion == 5:
                    print("Reclamar Pormoción 3")
                    ciclo  = 2
        else:
                    print("Escoja un opción valida")
                    
                    clear()
                    menu()
                    opcion = int(input("introduzca su tipo de pan favorito:"))
                


