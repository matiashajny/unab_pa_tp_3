class Punto:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def impresion(self):
        print(self.x,self.y)

    def eje_x(self):
        return self.x
    
    def eje_y(self):
        return self.y
    
    def mover(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    
class Linea:

    def __init__(self,punto_a,punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b

    def mueve_derecha(self, num):
        self.punto_a.mover(dx=num)
        self.punto_b.mover(dx=num)

    def mueve_izquierda(self, num):
        self.punto_a.mover(dx=-num)
        self.punto_b.mover(dx=-num)

    def mueve_arriba(self, num):
        self.punto_a.mover(dy=num)
        self.punto_b.mover(dy=num)

    def mueve_abajo(self, num):
        self.punto_a.mover(dy=-num)
        self.punto_b.mover(dy=-num)

    def impresion_linea(self):
        print("punto a: ")
        print(self.punto_a.x, self.punto_a.y)
        print()
        print("punto b: ")
        print(self.punto_b.x, self.punto_b.y)
        print()

punto_1 = Punto(1,3)
punto_2 = Punto(5,9)
linea_1 = Linea(punto_1,punto_2)

punto_1.impresion()
punto_1.eje_x()
punto_2.impresion()

linea_1.impresion_linea()
linea_1.mueve_derecha(2)
linea_1.impresion_linea()
linea_1.mueve_abajo(3)
linea_1.impresion_linea()
