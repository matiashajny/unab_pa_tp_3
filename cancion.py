class Cancion:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        print("Titulo de la cancion: ",self.titulo)
    
    def get_autor(self):
        print("Autor de la cancion: ",self.autor)
    
    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self.autor = nuevo_autor

cancion_1 = Cancion("Un Lago en el cielo", "Cerati")

cancion_1.get_titulo()
cancion_1.get_autor()

cancion_1.set_titulo("Wonderwall")
cancion_1.set_autor("Oasis")

cancion_1.get_titulo()
cancion_1.get_autor()
