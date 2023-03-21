
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


    
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
        opcion = int(input("Introduzca la opción a elegir:"))

        if opcion == 1:
                    print("Registrar Cliente")
                    from Menu import puntos
                    cliente1 = puntos.Cliente("XXX",0,"XXX")
                    cliente1.registrar()
                    ciclo  = 2
        elif opcion == 2:
                    print("Actualizar Puntos")
                    ciclo  = 2
        elif opcion == 3:
                    print("Reclamar Promoción 1")
                    ciclo  = 2
        elif opcion == 4:
                    print("Reclamar Promoción 2")
                    ciclo  = 2
        elif opcion == 5:
                    print("Reclamar Promoción 3")
                    ciclo  = 2
        elif opcion < 1 or opcion > 5:
                    clear()
                    menu()
                    print('Opción incorrecta.\n')
                    opcion = 1
                


