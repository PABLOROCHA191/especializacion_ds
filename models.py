class Libro:
    def __init__(self, titulo, autor, isbn, genero, anio_publicacion, disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.disponible = disponible

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

class Prestamo:
    def __init__(self, id_usuario, titulo_libro, fecha_prestamo, fecha_devolucion, devuelto):
        self.id_usuario = id_usuario
        self.titulo_libro = titulo_libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = devuelto