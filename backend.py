import json  # Archivos JSON
import requests  # API

# Variables de acciones principales: Tuplas definidas para poder hacer la comparación con lo ingresado por el usuario
opcion_visualizar = (1, ' - ', 'Visualizar')
opcion_registrar = (2, ' - ', 'Registrar')
opcion_modificar = (3, ' - ', 'Modificar')
opcion_eliminar = (4, ' - ', 'Eliminar')
opcion_buscar = (5, ' - ', 'Buscar')
opcion_buscar_API_Google = (6, ' - ', 'Buscar en API de Google Books')

# Variables de acciones secundarias: Tuplas definidas para poder hacer la comparación con lo ingresado por el usuario
opcion_libro = (1, ' - ', 'Libro')
opcion_socio = (2, ' - ', 'Socio')
opcion_prestamo = (3, ' - ', 'Prestamo')

# Comienzo del programa:
h1 = 'Bienvenido al sistema de registros de la Biblioteca.'
h2 = '¿Qué desea realizar?'
h3 = 'Acciones: Visualizar - Registrar - Modificar - Eliminar - Buscar - Buscar en Google API'
h4 = 'Por: Libros - Socios - Prestamos'
h5 = '(Ej: Visualizar: Libros)'

# Función para procesar la opción ingresada por el usuario
def procesar_opcion(opcion):
    if opcion == "Visualizar: Libros":
        return visualizar_libros()
    else:
        return "Opción no válida"

# Funciones para cada opción específica
def visualizar_libros():
    # Lógica para visualizar libros
    # return "Llamando a la función para Visualizar Libros"
    
    data = abrir_archivos('json/libros.json')

    return recorrer_archivo(data)


# Función para abrir archivos: Esta función es para poder abrir los archivos JSON (libros, socios, prestamos) leerlos y devolver el contenido. 
def abrir_archivos(archivo): 
    with open(archivo) as archivo: # Por parámetro se envía la ruta del archivo .json 
        data = json.load(archivo) # Carga el archivo para poder utilizarlo y lo guarda en la variable data
    return data # Retorna los datos del archivo .json

def recorrer_archivo(archivo):
    resultados = []
    for elemento in archivo:
        for clave, valor in elemento.items():
            resultados.append(f'{clave}: {valor}')
    
    return "\n".join(resultados)
