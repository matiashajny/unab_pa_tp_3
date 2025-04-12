class Libro:

    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, lugar, fecha_edicion):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha_edicion = fecha_edicion

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_isbn(self):
        return self.isbn
    
    def get_paginas(self):
        return self.paginas
    
    def get_edicion(self):
        return self.edicion
    
    def get_editorial(self):
        return self.editorial
    
    def get_lugar(self):
        return self.lugar
    
    def get_fecha_edicion(self):
        return self.fecha_edicion
    
    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self.autor = nuevo_autor

    def set_isbn(self, nuevo_isbn):
        self.isbn = nuevo_isbn

    def set_paginas(self, cant_paginas):
        self.paginas = cant_paginas

    def set_edicion(self, nueva_edicion):
        self.edicion = nueva_edicion

    def set_editorial(self, nueva_editorial):
        self.editorial = nueva_editorial

    def set_lugar(self, nuevo_lugar):
        self.lugar = nuevo_lugar

    def set_fecha_edicion(self, nueva_fecha_edicion):
        self.fecha_edicion = nueva_fecha_edicion
    

    def mostrar_informacion(self):
        print("Titulo: ", self.titulo)
        print("Autor: ", self.autor)
        print("ISBN: ", self.isbn)
        print(self.lugar)
        print(self.fecha_edicion)
        print(self.paginas, "paginas")
        
libro_1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", "0-15-234632648-754", 138, "edicion Debolsillo","RBA" , "Buenos Aires, Argentina", "20/03/1992")

libro_1.mostrar_informacion()
