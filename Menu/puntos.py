
K = 1000
inicioCompra = 0

class Cliente:
    def __init__(self,nombre,telefono,correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
    
    def registrar(self):
        
        self.nombre = input("Escriba su nombre: ")
        
        self.telefono = int(input("Escriba su telefono: "))
        
        self.correo = input("Escriba su correo: ")
   
class Puntos(Cliente):

    def __init__(self, nombre, telefono, correo) -> None:
        super().__init__(nombre, telefono, correo)
        self.compra = inicioCompra
        self.puntos = []

    def conversion_puntos(self):
        self.compra = float(input("¿Total de la compra? "))
        self.puntos = self.compra/K

    def puntos_total(self):
        puntos = 0
        for i in self.puntos:
            puntos = i + puntos
        print(f"Los puntos que tiene en total son {puntos}") 

    def mostrar_puntos(self):
        print("Sus puntos en total son ",self.puntos)

    def menu_puntos(self):
        print("""
        ----------------MENU PUNTOS---------------------


        """)
cliente1 = Puntos("XXX",0,"XXXX")




print("Gracias por tu compra vuelve pronto")

