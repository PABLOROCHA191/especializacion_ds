try:
    from fastapi import FastAPI, HTTPException
    import pandas as pd
    from models import Libro, Usuario, Prestamo
    from datetime import date
    from Estrategia.estrategia_carga import CargaDesdeExcel
    from Estados.gestor_de_prestamos import GestorDePrestamos
except ImportError as e:
    print(f"Error importing modules: {e}")

app = FastAPI()

# Inicializar la biblioteca
class Biblioteca:
    def __init__(self, archivo_excel):
        self.libros = []
        self.usuarios = []
        self.prestamos = []
        self.cargar_datos_desde_excel(archivo_excel)

    def cargar_datos_desde_excel(self, archivo_excel):
        cargador = CargaDesdeExcel()
        self.libros, self.usuarios, self.prestamos = cargador.cargar_datos(archivo_excel)

biblioteca = Biblioteca("data/datos.xlsx")
gestor_prestamos = GestorDePrestamos(biblioteca)

# Endpoints para libros
@app.get("/libros")
def obtener_libros():
    return biblioteca.libros

@app.get("/libros/{titulo}")
def obtener_libro_por_titulo(titulo: str):
    libro = next((l for l in biblioteca.libros if l.titulo == titulo), None)
    if libro:
        return libro
    raise HTTPException(status_code=404, detail="Libro no encontrado")

# Endpoints para usuarios
@app.get("/usuarios")
def obtener_usuarios():
    return biblioteca.usuarios

@app.get("/usuarios/{id_usuario}")
def obtener_usuario_por_id(id_usuario: str):
    usuario = next((u for u in biblioteca.usuarios if u.id_usuario == id_usuario), None)
    if usuario:
        return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Endpoints para préstamos
@app.get("/prestamos")
def obtener_prestamos():
    return biblioteca.prestamos

@app.post("/prestamos")
def registrar_prestamo(id_usuario: str, titulo_libro: str, fecha_prestamo: date, fecha_devolucion: date):
    try:
        gestor_prestamos.registrar_prestamo(id_usuario, titulo_libro, fecha_prestamo, fecha_devolucion)
        return {"message": "Préstamo registrado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/prestamos/devolver/{titulo_libro}")
def registrar_devolucion(titulo_libro: str):
    try:
        gestor_prestamos.registrar_devolucion(titulo_libro)
        return {"message": "Devolución registrada con éxito"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))