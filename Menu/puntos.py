
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
        while self.compra < 0:
            print('Valor inválido:')
            self.compra = float(input("¿Total de la compra? "))
        self.puntoscompra = self.compra/K
        self.puntos.append(self.puntoscompra)

    def actualizar_puntos(self, actualizar_puntos):
        self.puntos.append(actualizar_puntos)
    def realizar_compra(self):
        print('COMPRA')
        self.conversion_puntos()
    def reclamar_promocion(self,promocion):
        puntos = 0
        puntos= sum(self.puntos)#el segundo parámetro señaliza el  inicio de la suma
        compras_totales = len(self.puntos)
        print(f"Los puntos que tiene en total son {puntos}, en un total de {compras_totales} compras realizadas")                       
        if puntos - promocion < 0:
            print("Reclamaste la promoción ")

    def mostrar_puntos(self):
        print("Sus puntos en total son ",self.puntos)

    def menu_puntos(self):
        print("""
        ----------------MENU PUNTOS---------------------


        """)
cliente1 = Puntos("XXX",0,"XXXX")
cliente2 = Puntos("XXX",0,"XXXX")





