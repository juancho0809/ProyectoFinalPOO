
K = 100
inicioCompra = 0
listaClientes=[]

class Cliente:
    def __init__(self,nombre,telefono,correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        
        
    def registrar(self, numero):
        
        self.nombre = input("Escriba su nombre: ")
        self.telefono = int(input("Escriba su telefono: "))
        self.correo = input("Escriba su correo: ")

        numero =+ 1
        self.cliente=[self.nombre,self.telefono,self.correo,0]
        input("Los datos recogidos son: ")
        listaClientes = [f'Cliente {numero}']
        listaClientes.extend(self.cliente)
        for i in range (len(listaClientes)):
            print(listaClientes[i])
        input("Enter para volver al menu...")
    
class Puntos(Cliente): 

    def __init__(self, nombre, telefono, correo,puntos) -> None:
        super().__init__(nombre, telefono, correo,)
        self.compra = inicioCompra
        self.puntos = []

    def puntos_total(self):
        puntos = 0
        for i in self.puntos:
            puntos = i + puntos
        print(f"Los puntos que tiene en total son {puntos}") 

    def agregar_puntos(self, actualizar_puntos):
        self.puntos.append(actualizar_puntos)

    def realizar_compra(self):
        
        print('COMPRA')
        self.compra = float(input("¿Total de la compra? "))
        while self.compra < 0:
            print('Valor inválido:')
            self.compra = float(input("¿Total de la compra? "))
        self.puntoscompra = self.compra/K
        self.agregar_puntos(self.puntoscompra)
        print(self.puntoscompra)
        self.puntos_total()
        input()

        
    def reclamar_promocion(self,promocion):
        
        self.promocion = int(input("¿Cuantos puntos tuvo en su ultima compra?"))
        
        #el segundo parámetro señaliza el  inicio de la suma                  
        if self.promocion - promocion > 0:
            decision = int(input("Puedes reclamar la promocion, ¿desea reclamarla ahora? 1) si, en caso contrario otro numero"))
            if decision == 1:
                print("ten tu promocion!!")
                self.promocion = self.promocion - promocion
            else:
                print("Te esperamos una proxima ocasion")
        else:
            print("No tiene puntos suficientes")
        input()
