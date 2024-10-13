# fabrica_entidades.py
from models import Libro, Usuario, Prestamo

class FabricaDeEntidades:
    @staticmethod
    def crear_libro(titulo, autor, isbn, genero, anio_publicacion, disponible):
        return Libro(titulo=titulo, autor=autor, isbn=isbn, genero=genero, anio_publicacion=anio_publicacion, disponible=disponible)

    @staticmethod
    def crear_usuario(nombre, id_usuario):
        return Usuario(nombre=nombre, id_usuario=id_usuario)

    @staticmethod
    def crear_prestamo(id_usuario, titulo_libro, fecha_prestamo, fecha_devolucion, devuelto):
        return Prestamo(id_usuario=id_usuario, titulo_libro=titulo_libro, fecha_prestamo=fecha_prestamo, fecha_devolucion=fecha_devolucion, devuelto=devuelto)

# estrategia_carga.py
from abc import ABC, abstractmethod

class EstrategiaCarga(ABC):
    @abstractmethod
    def cargar_datos(self, archivo):
        pass

# Estrategia para cargar datos desde Excel
class CargaDesdeExcel(EstrategiaCarga):
    def cargar_datos(self, archivo):
        # Lógica para cargar desde Excel
        pass

# Estrategia para cargar datos desde CSV
class CargaDesdeCSV(EstrategiaCarga):
    def cargar_datos(self, archivo):
        # Lógica para cargar desde CSV
        pass
class GestorDePrestamos:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

# estado_prestamo.py
from abc import ABC, abstractmethod

class EstadoPrestamo(ABC):
    @abstractmethod
    def manejar(self):
        pass

class PrestamoPendiente(EstadoPrestamo):
    def manejar(self):
        print("El préstamo está pendiente.")

class PrestamoActivo(EstadoPrestamo):
    def manejar(self):
        print("El préstamo está activo.")

class PrestamoDevuelto(EstadoPrestamo):
    def manejar(self):
        print("El préstamo ha sido devuelto.")