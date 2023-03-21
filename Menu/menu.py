
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def printMenu():  
    print("""

    Bienvenidos al Sistema de Distri Pizza

    Escoja la opción de su preferencia:

    1) Registrar Cliente

    2) Realizar Compra

    3) Reclamar Promocion 1

    4) Reclamar Promocion 2

    5) Reclamar Promoción 3

    6) Salir del Usuario

            """)
def opcion():       
    opcion = 0
    while opcion != 2023:
        printMenu()
        opcion = int(input("Introduzca la opción a elegir:"))

        if opcion == 1:
                    print("-----REGISTRAR USUARIO-----")
                    from Menu import puntos
                    cliente1 = puntos.Cliente("XXX",0,"XXX")
                    cliente1.registrar()
                    
        elif opcion == 2:
                    print("----REALIZAR COMPRA----")
                    from Menu import puntos
                    
                    cliente1 = puntos.Puntos("XXX",0,"XXX")
                    cliente1.realizar_compra()
                    
        elif opcion == 3:
                    print("----RECLAMAR PROMOCIÓN----")
                    from Menu import puntos
                    
                    cliente1 = puntos.Puntos("XXX",0,"XXX")
                    cliente1.reclamar_promocion(1500)
                    
        elif opcion == 4:
                    print("Reclamar Promoción 2")
                    
        elif opcion == 5:
                    print("Reclamar Promoción 3")
                    
        elif opcion == 6:
                    #log out
                    print("Salir usuario")
        elif opcion == 2023:#Opción para salir del sistema
            print('Ha salido del sistema') 
            exit()
        elif opcion < 1 or opcion > 7 or opcion==2023:#Validación opción
                    clear()                   
                    print('Opción incorrecta.\n')
                    opcion = 1
                   


