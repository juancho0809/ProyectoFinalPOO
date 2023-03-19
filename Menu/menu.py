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
    
    opcion = int(input("introduzca su tipo de pan favorito:"))

    if opcion == 1:
        print("pan baguette")
    if opcion == 2:
        print("pan hojaldrado")
    if opcion == 3:
        print("croissant")
    else:    
        print("pan no encontrado")



