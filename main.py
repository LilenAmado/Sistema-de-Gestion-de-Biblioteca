##################################################################################################################
##################################################################################################################
###################################################### Opción 2: #################################################
######################################### Sistema de Gestión de Bibliotecas ######################################
############################################ Autoría: Amado, Lién Anahí ##########################################
##################################################################################################################

import json # Archivos JSON
import requests # API

##################################################################################################################
########################################## Variables principales (tuplas): #######################################
##################################################################################################################

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

##################################################################################################################
############################################## Funciones auxiliares: #############################################
##################################################################################################################

# Función para realizar separadores en la consola (para un mejor entendimiento en el resultado): 
def separador(elemento): # Pide por pantalla que tipo de separador quiere, si con '_', '-' o '*' 
    print(elemento * 60) # Lo multiplica por 60 para que se muestre una línea bastante larga de separador entre lo mostrado por pantalla. 


# Función para definir si la variable (valor ingresado por consola) es un número entero:
def es_numero(opcion):
    while True:
        if opcion.isdigit() and int(opcion) > 0: # Poder visualizar si ingresó el usuario un número a la variable 
            return int(opcion) # Retorna la transformación de la variable en número entero
        elif opcion == '': # Evaluamos si la variable se encuentra vacía
            opcion = input("No ingresó nada. Ingrese una opción válida (número entero positivo): ")
        else: # Sino es un digito o no se encuentra vacia, por ejemplo tiene otros caracteres, devuelve lo sig:
            opcion = input("Entrada inválida. Ingrese una opción válida (número entero positivo): ")


#****************************************** Función de archivos JSON: *******************************************#

# Función para abrir archivos: Esta función es para poder abrir los archivos JSON (libros, socios, prestamos) leerlos y devolver el contenido. 
def abrir_archivos(archivo): 
    with open(archivo) as archivo: # Por parámetro se envía la ruta del archivo .json 
        data = json.load(archivo) # Carga el archivo para poder utilizarlo y lo guarda en la variable data
    return data # Retorna los datos del archivo .json


# Función para escribir archivos: Esta función es para poder escribir los archivos JSON (libros, socios, prestamos).
def escribir_archivos(archivo, data): 
    with open(archivo, 'w') as archivo: # archivo = ruta del .json, "w" para escribir el archivo
        data = json.dump(data, archivo, indent=4) # Escribe los nuevos datos actualizados de la lista en el archivo .json. Data (nuevos datos que va a sobreescribir), archivo (ruta del .json), indent = 4 (para que el código resultante en .json sea más legible)


# Función para recorrer los archivos: Esta función es para poder recorrer con un for cada uno de los contenidos del archivo .json.  
def recorrer_archivo(archivo):
    for elemento in archivo: # Es para iterar cada uno de los elementos del archivo .json  
        for clave, valor in elemento.items(): # Itera sobre cada uno de los valores del diccionario, tanto la clave como el valor,
            print(f'{clave}: {valor}') # Los muestra por pantalla a cada valor
        separador("-") # Luego genera un separador


# Función para verificar si un libro, socio o prestamo existe:
def existe_contenido(num_id_archivo, archivo, id): # num_id_archivo: Num. de id dentro del archivo .json, archivo (ej: 'json/socios.json'), id del archivo (id_libro/id_socio/id_prestamo)
    for contenido in archivo: # Itera sobre cada socio, libro o prestamo en el diccionario dado en "archivo"
        if contenido[id] == num_id_archivo: # Verifica si el ID del socio, libro o prestamo actual coincide con el numero de id dado por el usuario
            return True # Si encuentra una coincidencia, retorna True indicando que el socio, libro o prestamo existe
    return False # Si no encuentra ninguna coincidencia, retorna False indicando que no existe


# Función para buscar un libro, socio o prestamo por id:
def buscar_por_id(num_id_archivo, archivo, id): # num_id_archivo: Num. de id dentro del archivo .json, archivo (ej: 'json/socios.json'), id del archivo (id_libro/id_socio/id_prestamo)
    for contenido in archivo: # Itera sobre cada socio, libro o prestamo en el diccionario dado en "archivo"
        if contenido[id] == num_id_archivo: # Verifica si el ID del socio, libro o prestamo actual coincide con el numero de id dado por el usuario
            return contenido # Retorna el contenido
    return None 


# Función para buscar un libro en la API de Google Books:
def buscar_biblioteca_google():
    GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes" # URL de la API de Google Books

    separador('*')
    print("Búsqueda de libros en la Biblioteca de Google:")
    separador('*')
    usuario_biblioteca_google = input("¿Qué tema quiere buscar?: ") # Pedido al usuario de qué necesita buscar
    cant_resultados = input("¿Cuánta cantidad de resultados desea ver?: ") 
    cant_resultados = es_numero(cant_resultados)

    # Parámetros para la búsqueda
    params = { # Diccionario de Python que se utiliza para almacenar los parámetros que se envian en la solicitud HTTP a la API de Google Books.
        'q': usuario_biblioteca_google,  # Variable ingresada por el usuario para la busqueda
        'maxResults': cant_resultados    # Variable ingresada por el usuario de la cantidad max de resultados que aparezcan por consola.
    }

    # Hacer la solicitud GET a la API: Una solicitud GET es un tipo de solicitud HTTP que se utiliza para obtener datos de un recurso específico a través de una URL desde el servidor de la API.
    response = requests.get(GOOGLE_BOOKS_API_URL, params=params)

    # Si se obtiene respuesta
    if response.status_code == 200:
        
        data_libro = response.json() # Convertir la respuesta JSON en un diccionario de Python

        separador("*") # Separador en consola

        for item in data_libro['items']: # Este bucle lo que hace es iterar en la lista de los libros encontrados en la API, data_libro['items']. 

            volume_info = item['volumeInfo'] 
            id = item.get('id')
            titulo = volume_info.get('title')
            autor = volume_info.get('authors', [])
            fecha_publicacion = volume_info.get('publishedDate')
            descripcion = volume_info.get('description')

            # Mostrar la información de los libros pedidos por consola:
            print(f"ID: {id}")
            print(f"Título: {titulo}")
            print(f"Autor: {', '.join(autor)}")
            print(f"Fecha de publicación: {fecha_publicacion}")
            print(f"Descripción: {descripcion}")

            separador('-')

    else:
        print(f"Error: {response.status_code}")

##################################################################################################################
############################################ Funciones principales: ##############################################
##################################################################################################################

# Función para elegir Libro, Socio o Prestamo: 
def seleccionar_opcion_SLP(palabra):
    while True:
        opcion = input(f'¿Qué desea {palabra}? Elija una de las siguientes opciones: (1 - Libro, 2 - Socio, 3 - Prestamo): ') # Pide al usuario que elija un número de libro, socio o prestamo
        opcion_usuario_accion_secundaria = es_numero(opcion) # Verifica si es un número
        if opcion_usuario_accion_secundaria == 1: # Si eligió opción 1: 
            print(f'Ha elegido la opción: {opcion_libro[2]}') # Muestra a consola la opción elegida
            return opcion_libro # Retorna la tupla que eligió el usuario, esta tupla esta definida en la variable al principio del código
        elif opcion_usuario_accion_secundaria == 2:
            print(f'Ha elegido la opción: {opcion_socio[2]}')
            return opcion_socio
        elif opcion_usuario_accion_secundaria == 3:
            print(f'Ha elegido la opción: {opcion_prestamo[2]}')
            return opcion_prestamo
        else:
            print('Opción inválida. Por favor, elija una opción válida.')


# Función para elegir una acción - Visualizar, Registrar, Modificar o Eliminar: 
def seleccionar_opcion(opcion_usuario): # La opción_usuario pedido por parámetro es el número de acción que eligió el usuario
    if opcion_usuario == 1: # Si eligió la opción 1: devolverá la tupla perteneciente a visualizar y llamará a la función anteriormente explicada enviando el valor 3 de la tupla (opcion_visualizar = (1, ' - ', 'Visualizar'))
        return opcion_visualizar, seleccionar_opcion_SLP(opcion_visualizar[2])

    elif opcion_usuario == 2: 
        return opcion_registrar, seleccionar_opcion_SLP(opcion_registrar[2])
    
    elif opcion_usuario == 3: 
        return opcion_modificar, seleccionar_opcion_SLP(opcion_modificar[2])
    
    elif opcion_usuario == 4: 
        return opcion_eliminar, seleccionar_opcion_SLP(opcion_eliminar[2])
    
    elif opcion_usuario == 5: 
        return opcion_buscar, seleccionar_opcion_SLP(opcion_buscar[2])
    
    elif opcion_usuario == 6:
        buscar_biblioteca_google()
        
    else:
        opcion = input('1 - Visualizar, 2 - Registrar, 3 - Modificar, 4 - Eliminar, 5 - Buscar, 6 - Buscar libro en biblioteca de Google: ')
        opcion_usuario = es_numero(opcion)
        return seleccionar_opcion(opcion_usuario) # Función recursiva: Vuelve a llamarse si es que no eligió ninguna opción válida.

#****************************************** Funciones de Acciones: *******************************************#   

#************************************************ Visualizar: ************************************************#

# Acción - Visualizar: Si el usuario elije la opción de visualizar un archivo:
def visualizar():
    if (accion_secundaria == opcion_socio): # accion_secundaria (opción elegida por el usuario (socio, libro o prestamo)) es igual a opcion_socio (socio en este caso)) llama la siguiente opción: 
        visualizar_archivo('Socios', 'json/socios.json')

    elif (accion_secundaria == opcion_libro): 
        visualizar_archivo('Libros', 'json/libros.json')

    elif (accion_secundaria == opcion_prestamo): 
        visualizar_archivo('Prestamos', 'json/prestamos.json')


# Visualizar archivo: 
def visualizar_archivo(nombre, archivo): # nombre: nombre del archivo que el usuario quiere visualizar. archivo: pasa la ruta del archivo que el usuario quiere visualizar
    separador("*") # Separador (linea) en la consola
    print(f'Lista de {nombre}: ') # Título
    separador("*") # Separador (linea) en la consola

    archivo = abrir_archivos(archivo) # Llama la función para abrir el archivo
    return recorrer_archivo(archivo) # Retorna la función que recorre el archivo enviado por parámetro


#************************************************ Registrar: ****************************************************#

# Acción - Registrar: Si el usuario elije la opción de registrar en el archivo:
def registrar():

    if accion_secundaria == opcion_socio: # Si accion_secundaria (opción elegida por el usuario (socio) es igual a opcion_socio (la tupla)): 

        data = abrir_archivos('json/socios.json') # Llama a la función para abrir el archivo
        
        # Condicional: Si data no está vacía, se busca el mayor valor de id_socio en la lista de diccionarios para autoincrementar el nuevo ID. Si data está vacía, se establece ultimo_id en 0

        # Si data tiene contenido: 
        if data:
            ultimo_id = max(socio["id_socio"] for socio in data if "id_socio" in socio) # Ultimo_id: se itera en el archivo pasado (json/socios.json) y sobre eso se toma el máximo id_socio. 
        else:
            ultimo_id = 0 # Sino le asigna el num 0
        
        # Pedido de valores al usuario:
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        fecha_nacimiento = input("Fecha de Nacimiento (Ejemplo: 1990-11-15): ")
        direccion = input("Dirección: ")
        correo_electronico = input("Correo Electronico: ")
        telefono = input("Telefono: ")

        # El último id le suma 1 más para generar el próximo:
        nuevo_id = ultimo_id + 1

        # Los valores ingresados al usuario se los "ubica" como valor a las claves: 
        nuevo_socio = {
            "id_socio": nuevo_id,
            "nombre": nombre,
            "apellido": apellido,
            "fecha_nacimiento": fecha_nacimiento,
            "direccion": direccion,
            "correo_electronico": correo_electronico,
            "telefono": telefono
        }

        # Se utiliza la función append para agregar los nuevos valores: 
        data.append(nuevo_socio)
        
        # Se llama a la función para escribir con el nuevo valor en el archivo socios: 
        data = escribir_archivos('json/socios.json', data)

        separador("-")
        print("Nuevo socio registrado exitosamente.")
        separador("-")

    elif (accion_secundaria == opcion_libro): # Si accion_secundaria (opción elegida por el usuario (libro) es igual a opcion_libro (la tupla)): 

        data = abrir_archivos('json/libros.json') # Llama a la función para abrir el archivo
        
        # Condicional: Si data no está vacía, se busca el mayor valor de id_libro en la lista de diccionarios para autoincrementar el nuevo ID. Si data está vacía, se establece ultimo_id en 0
        # Si data tiene contenido: 
        if data:
            ultimo_id = max(libro["id_libro"] for libro in data if "id_libro" in libro) # Ultimo_id: se itera en el archivo pasado (json/libros.json) y sobre eso se toma el máximo id_libro.
        else:
            ultimo_id = 0 # Sino le asigna el num 0
        
        # Pedido de valores al usuario:
        titulo = input("Título: ")
        autor = input("Autor: ")
        editorial = input("Editorial: ")
        año_publicacion = input("Año publicación: ")
        genero = input("Género: ")
        cantidad_disponible = input("Cantidad disponible: ")

        # El último id le suma 1 más para generar el próximo:
        nuevo_id = ultimo_id + 1

        # Los valores ingresados al usuario se los "ubica" como valor a las claves: 
        nuevo_libro = {
            "id_libro": nuevo_id,
            "titulo": titulo,
            "autor": autor,
            "editorial": editorial,
            "año_publicacion": año_publicacion,
            "genero": genero,
            "cantidad_disponible": cantidad_disponible
        }

        # Se utiliza la función append para agregar los nuevos valores: 
        data.append(nuevo_libro)
        
        # Se llama a la función para escribir con el nuevo valor en el archivo libros: 
        data = escribir_archivos('json/libros.json', data)

        separador("-")
        print("Nuevo libro registrado exitosamente.")
        separador("-")

    elif (accion_secundaria == opcion_prestamo): # Si accion_secundaria (opción elegida por el usuario (prestamo) es igual a opcion_prestamo (la tupla)): 

        # Abre los 3 archivos:
        prestamos = abrir_archivos('json/prestamos.json')
        socios = abrir_archivos('json/socios.json')
        libros = abrir_archivos('json/libros.json')

        # Condicional: Si data no está vacía, se busca el mayor valor de id_libro en la lista de diccionarios para autoincrementar el nuevo ID. Si data está vacía, se establece ultimo_id en 0
        # Si prestamos tiene contenido: 
        if prestamos:
            ultimo_id_prestamo = max(prestamo["id_prestamo"] for prestamo in prestamos if "id_prestamo" in prestamo) # ultimo_id_prestamo: se itera en el archivo pasado (json/prestamos.json) y sobre eso se toma el máximo id_prestamo.
        else:
            ultimo_id_prestamo = 0 # Sino le asigna el num 0
        
        # Pedido de valores al usuario:
        id_socio = input("ID del socio: ")
        id_socio = es_numero(id_socio) # Evalua si es un número
        id_libro = input("ID del libro: ")
        id_libro = es_numero(id_libro) # Evalua si es un número
        fecha_prestamo = input("Fecha de préstamo (Ejemplo: 2023-06-12): ")
        fecha_devolucion = input("Fecha de devolución (Ejemplo: 2023-06-19): ")
        estado_prestamo = input("Estado del préstamo (Ejemplo: Devuelto / En Curso): ")

        # Condicional creado para que verificar que elija una de las dos opciones (En Curso o Devuelto):
        while estado_prestamo != "Devuelto" and estado_prestamo != "En Curso":
            estado_prestamo = input("Estado del préstamo (Ejemplo: Devuelto / En Curso): ")

        # Función para verificar la existencia de los id pedidos al usuario de libro y socio: Si es true ingresa al condicional.
        if existe_contenido(id_socio, socios, "id_socio") and existe_contenido(id_libro, libros, "id_libro"):
            # id_socio y id_libro pedidos al usuario, socios y libros: ruta .json. 

            # El último id le suma 1 más para generar el próximo:
            nuevo_id_prestamo = ultimo_id_prestamo + 1
                
            # Los valores ingresados al usuario se los "ubica" como valor a las claves: 
            nuevo_prestamo = {
                "id_prestamo": nuevo_id_prestamo,
                "id_socio": id_socio,
                "id_libro": id_libro,
                "fecha_prestamo": fecha_prestamo,
                "fecha_devolucion": fecha_devolucion,
                "estado_prestamo": estado_prestamo
            }

            # Se utiliza la función append para agregar los nuevos valores: 
            prestamos.append(nuevo_prestamo)
            
            # Se llama a la función para escribir con el nuevo valor en el archivo prestamos: 
            escribir_archivos('json/prestamos.json', prestamos)

            separador("-")
            print("Nuevo prestamo registrado exitosamente.")
            separador("-")
        else:
            separador("-")
            print("El ID del socio o el ID del libro no existen. Por favor, verifique e intente nuevamente.")
            separador("-")
 

#************************************************ Modificar: ****************************************************#

# Acción - Modificar: Si el usuario elije la opción de modificar el archivo:
def modificar():

    if accion_secundaria == opcion_socio: # accion_secundaria (opción elegida por el usuario (socio, libro o prestamo)) es igual a opcion_socio (socio en este caso)) llama la siguiente opción: 

        socios = abrir_archivos('json/socios.json') # Abrir archivo socios

        id_socio = input("Ingrese el ID del socio a modificar: ") # Pedir al usuario el valor del id perteneciente al socio que desea modificar
        id_socio = es_numero(id_socio) # Verificar si es un numero

        # Verificar si existe el número ingresado de id por el usuario, id_socio (ingresado por el usuario), socios (ruta .json), "id_socio" para poder iterar en esa clave y ver si se encuentra en el archivo tal valor:
        if existe_contenido(id_socio, socios, "id_socio"):
            for socio in socios: # Iterar sobre el archivo .json

                if socio["id_socio"] == id_socio: # Si el valor ingresado por el usuario y la clave del dicc. son iguales: 

                    # Guarda nuevos valores a las variables:
                    print("Datos actuales del socio (dejar vacío para no modificar):")
                    nombre = input("Nuevo Nombre: ")
                    apellido = input("Nuevo Apellido: ")
                    fecha_nacimiento = input("Nueva Fecha de Nacimiento (Ejemplo: 1990-11-15): ")
                    direccion = input("Nueva Dirección: ")
                    correo_electronico = input("Nuevo Correo Electronico: ")
                    telefono = input("Nuevo Telefono: ")

                    # Asigna nuevos valores a cada clave:valor. Si hay contenido ingresa, si el contenido es vacío es false asique no ingresa: 
                    if nombre:
                        socio["nombre"] = nombre
                    if apellido:
                        socio["apellido"] = apellido
                    if fecha_nacimiento:
                        socio["fecha_nacimiento"] = fecha_nacimiento
                    if direccion:
                        socio["direccion"] = direccion
                    if correo_electronico:
                        socio["correo_electronico"] = correo_electronico
                    if telefono:
                        socio["telefono"] = telefono

                    escribir_archivos('json/socios.json', socios) # Se llama a la función para escribir con el nuevo valor en el archivo socios:
                    print("Socio modificado exitosamente.")
                    break
        else:
            print("El ID del socio no existe.")

    elif accion_secundaria == opcion_libro:  # accion_secundaria (opción elegida por el usuario (socio, libro o prestamo)) es igual a opcion_libro (libros en este caso)) llama la siguiente opción: 

        libros = abrir_archivos('json/libros.json') # Abrir archivo libros

        id_libro = input("Ingrese el ID del libro a modificar: ") # Pedir al usuario el valor del id perteneciente al libro que desea modificar
        id_libro = es_numero(id_libro) # Verificar si es un número

        # Verificar si existe el número ingresado de id por el usuario, id_libro (ingresado por el usuario), socios (ruta .json), "id_libro" para poder iterar en esa clave y ver si se encuentra en el archivo tal valor:
        if existe_contenido(id_libro, libros, "id_libro"):

            for libro in libros: # Iterar sobre el archivo .json

                if "id_libro" in libro and libro["id_libro"] == id_libro: # Si el valor ingresado por el usuario y la clave del dicc. son iguales

                    # Guarda nuevos valores a las variables:
                    print("Datos actuales del libro (dejar vacío para no modificar): ")
                    print(libro)
                    titulo = input("Nuevo Título: ")
                    autor = input("Nuevo Autor: ")
                    editorial = input("Nueva Editorial: ")
                    año_publicacion = input("Nuevo Año publicación: ")
                    genero = input("Nuevo Género: ")
                    cantidad_disponible = input("Nueva Cantidad disponible: ")

                    # Asigna nuevos valores a cada clave:valor. Si hay contenido ingresa, si el contenido es vacío es false asique no ingresa: 
                    if titulo:
                        libro["titulo"] = titulo
                    if autor:
                        libro["autor"] = autor
                    if editorial:
                        libro["editorial"] = editorial
                    if año_publicacion:
                        libro["año_publicacion"] = año_publicacion
                    if genero:
                        libro["genero"] = genero
                    if cantidad_disponible:
                        libro["cantidad_disponible"] = cantidad_disponible

                    escribir_archivos('json/libros.json', libros) # Se llama a la función para escribir con el nuevo valor en el archivo libros

                    print("Libro modificado exitosamente.")
                    break
        else:
            print("El ID del libro no existe.")

    elif accion_secundaria == opcion_prestamo: # accion_secundaria (opción elegida por el usuario (socio, libro o prestamo)) es igual a opcion_prestamos (prestamos en este caso)) llama la siguiente opción: 

        prestamos = abrir_archivos('json/prestamos.json') # Abrir archivo prestamos

        id_prestamo = input("Ingrese el ID del préstamo a modificar: ")# Pedir al usuario el valor del id perteneciente al prestamo que desea modificar
        id_prestamo = es_numero(id_prestamo) # Verificar si es un número

        if any(prestamo["id_prestamo"] == id_prestamo for prestamo in prestamos): 

            for prestamo in prestamos: # Itera sobre el archivo .json

                if prestamo["id_prestamo"] == id_prestamo: # Si el valor ingresado por el usuario y la clave del dicc. son iguales

                    # Guarda nuevos valores a las variables:
                    print("Datos actuales del préstamo:")
                    print(prestamo)
                    id_socio = input("Nuevo ID de socio (dejar vacío para no modificar): ")
                    id_libro = input("Nuevo ID de libro (dejar vacío para no modificar): ")
                    fecha_prestamo = input("Nueva Fecha de préstamo (dejar vacío para no modificar): ")
                    fecha_devolucion = input("Nueva Fecha de devolución (dejar vacío para no modificar): ")
                    estado_prestamo = input("Nuevo Estado del préstamo (dejar vacío para no modificar): ")

                    # Asigna nuevos valores a cada clave:valor. Si hay contenido ingresa, si el contenido es vacío es false asique no ingresa: 
                    if id_socio:
                        prestamo["id_socio"] = es_numero(id_socio)
                    if id_libro:
                        prestamo["id_libro"] = es_numero(id_libro)
                    if fecha_prestamo:
                        prestamo["fecha_prestamo"] = fecha_prestamo
                    if fecha_devolucion:
                        prestamo["fecha_devolucion"] = fecha_devolucion
                    if estado_prestamo:
                        prestamo["estado_prestamo"] = estado_prestamo

                    escribir_archivos('json/prestamos.json', prestamos) # Se llama a la función para escribir con el nuevo valor en el archivo prestamos

                    print("Préstamo modificado exitosamente.")
                    break
        else:
            print("El ID del préstamo no existe.")

#************************************************* Eliminar: ****************************************************#

# Acción - Eliminar: Si el usuario elije la opción de eliminar el archivo:
def eliminar(): 

    if accion_secundaria == opcion_socio: # accion_secundaria (opción elegida por el usuario (socio, libro o prestamo)) es igual a opcion_socio (socio en este caso)) llama la siguiente opción:

        socios = abrir_archivos('json/socios.json') # Abrir archivo prestamos

        id_socio = input("Ingrese el ID del socio a eliminar: ") # Pedir al usuario el valor del id perteneciente al socio que desea eliminar
        id_socio = es_numero(id_socio) # Verificar si es un número válido

        # Verificar si existe el número ingresado de id por el usuario, id_socio (ingresado por el usuario), socios (ruta .json), "id_socio" para poder iterar en esa clave y ver si se encuentra en el archivo tal valor:
        if existe_contenido(id_socio, socios, "id_socio"):
            socios = [socio for socio in socios if socio["id_socio"] != id_socio] # Filtrar la lista de socios para eliminar el socio que el ID coincide con el ID ingresado
            escribir_archivos('json/socios.json', socios) # Llama la función para escribir la lista actualizada de socios de nuevo en el archivo 'socios.json'
            print("Socio eliminado exitosamente.")
        else:
            print("El ID del socio no existe.")

    elif accion_secundaria == opcion_libro: # accion_secundaria (opción elegida por el usuario (socio, libro o prestamo)) es igual a opcion_libro (libro en este caso)) llama la siguiente opción

        libros = abrir_archivos('json/libros.json') # Abrir archivo prestamos

        id_libro = input("Ingrese el ID del libro a eliminar: ") # Pedir al usuario el valor del id perteneciente al libro que desea eliminar
        id_libro = es_numero(id_libro) # Verificar si es un número válido

        # Verificar si existe el número ingresado de id por el libro, id_libro (ingresado por el usuario), libros (ruta .json), "id_libro" para poder iterar en esa clave y ver si se encuentra en el archivo tal valor:
        if existe_contenido(id_libro, libros, "id_libro"):
            libros = [libro for libro in libros if libro["id_libro"] != id_libro] # Filtrar la lista de libros para eliminar el libro que el ID coincide con el ID ingresado
            escribir_archivos('json/libros.json', libros) # Llama la función para escribir la lista actualizada de libros de nuevo en el archivo 'libros.json'
            print("Libro eliminado exitosamente.")
        else:
            print("El ID del libro no existe.")

    elif accion_secundaria == opcion_prestamo: # accion_secundaria (opción elegida por el usuario (socio, libro o prestamo)) es igual a opcion_prestamo (prestamo en este caso)) llama la siguiente opción

        prestamos = abrir_archivos('json/prestamos.json') # Abrir archivo prestamos

        id_prestamo = input("Ingrese el ID del préstamo a eliminar: ") # Pedir al usuario el valor del id perteneciente al libro que desea eliminar
        id_prestamo = es_numero(id_prestamo) # Verificar si es un número válido

        if any(prestamo["id_prestamo"] == id_prestamo for prestamo in prestamos): # Verifica si existe un préstamo con el ID ingresado

            prestamos = [prestamo for prestamo in prestamos if prestamo["id_prestamo"] != id_prestamo] # Filtrar la lista de préstamos para eliminar el préstamo que el ID coincide con el ID ingresado
            escribir_archivos('json/prestamos.json', prestamos) # Llama la función para escribir la lista actualizada de prestamos de nuevo en el archivo 'prestamos.json'
            print("Préstamo eliminado exitosamente.")
        else:
            print("El ID del préstamo no existe.")

#************************************************* Buscar: ****************************************************#

# Acción - Buscar: Si el usuario elije la opción de buscar el archivo:

def buscar():

    if accion_secundaria == opcion_socio: # accion_secundaria (opción elegida por el usuario (socio, libro o prestamo)) es igual a opcion_socio (socio en este caso)) llama la siguiente opción
        
        socios = abrir_archivos('json/socios.json') # Abrir archivo .json

        id_socio_a_buscar = input("Buscar socio por número de id: ") # Pedir al usuario el valor del id perteneciente al socio que desea buscar

        separador("-")

        id_socio_a_buscar = es_numero(id_socio_a_buscar) # Verifica si el número es válido

        socio_encontrado = buscar_por_id(id_socio_a_buscar, socios, "id_socio") # Busca el número ingresado de id (id_socio_a_buscar) ingresado por el usuario), socios (ruta .json), "id_socio" para poder iterar en esa clave y ver si se encuentra en el archivo 

        if socio_encontrado: # Si el socio fue encontrado (true)
            for clave, valor in socio_encontrado.items():
                print(f'{clave.upper()}: {valor}') # Muestra los detalles del socio encontrado

        else:
            print("Socio no encontrado.")

    elif accion_secundaria == opcion_libro: # accion_secundaria (opción elegida por el usuario (socio, libro o prestamo)) es igual a opcion_libro (libro en este caso)) llama la siguiente opción

        libros = abrir_archivos('json/libros.json') # Abrir archivo .json

        id_libro_a_buscar = input("Buscar libro por número de id: ") # Pedir al usuario el valor del id perteneciente al libro que desea buscar

        separador("-")

        id_libro_a_buscar = es_numero(id_libro_a_buscar) # Verificar si el número es válido

        libro_encontrado = buscar_por_id(id_libro_a_buscar, libros, "id_libro") # Busca el número ingresado de id (id_libro_a_buscar) ingresado por el usuario, libros (ruta .json), "id_libro" para poder iterar en esa clave y ver si se encuentra en el archivo 

        if libro_encontrado: # Si el socio fue encontrado (true)

            for clave, valor in libro_encontrado.items():
                print(f'{clave.upper()}: {valor}') # Muestra los detalles del libro encontrado

        else:
            print("Libro no encontrado.")

    elif accion_secundaria == opcion_prestamo: # accion_secundaria (opción elegida por el usuario (socio, libro o prestamo)) es igual a opcion_prestamo (prestamo en este caso)) llama la siguiente opción

        prestamos = abrir_archivos('json/prestamos.json') # Abrir archivo .json

        id_prestamo_a_buscar = input("Buscar préstamo por número de id: ") # Pedir al usuario el valor del id perteneciente al prestamo que desea buscar

        separador("-")

        id_prestamo_a_buscar = es_numero(id_prestamo_a_buscar) # Verificar si es un número válido

        prestamo_encontrado = buscar_por_id(id_prestamo_a_buscar, prestamos, "id_prestamo") # Busca el número ingresado de id (id_prestamo_a_buscar) ingresado por el usuario, prestamos (ruta .json), "id_prestamo" para poder iterar en esa clave y ver si se encuentra en el archivo 

        if prestamo_encontrado: # Si el préstamo fue encontrado (true)

            for clave, valor in prestamo_encontrado.items():
                print(f'{clave.upper()}: {valor}') # Muestra los detalles del prestamo encontrado

        else:
            print("Préstamo no encontrado.")


####################################################################################################
########################################## App/Programa: ###########################################
####################################################################################################

# Comienzo del programa:
print('Bienvenido al sistema de registros de la Biblioteca.') 
# Variable para iniciar o no el programa:
accion = input('¿Desea iniciar una acción? De ser así escriba "Iniciar" de lo contrario escribir "Fin": ')

while True: # Para que cuando termine el programa vuelva a iniciar cuantas veces sea necesario
    
    if accion == "Iniciar" or accion == "iniciar" or accion == "INICIAR": # Si el valor de la variable accion es Iniciar, comience el programa:

        print('¿Qué desea realizar? Elija una opción (ingrese número),')

        # Ingreso del usuario:
        opcion = input('1 - Visualizar, 2 - Registrar, 3 - Modificar, 4 - Eliminar, 5 - Buscar, 6 - Buscar libro en biblioteca de Google: ')

        # Verifica si el valor es un número válido:
        opcion_usuario = es_numero(opcion)

        if opcion_usuario == 6: # Si la opcion del usuario es 6:
            accion_principal = seleccionar_opcion(opcion_usuario) # Llama la función seleccionar_opcion enviando la opción elegida por el usuario. API
        else: 
            # Tupla con la acción principal y secundaria del programa y llama la función seleccionar_opcion enviando la opción del usuario:
            accion_principal, accion_secundaria = seleccionar_opcion(opcion_usuario) 

            separador("_")
            
            print(f'Opciones seleccionadas fueron: {accion_principal[2].upper()} el archivo {accion_secundaria[2].upper()}') # Resultado de la elección del usuario

            separador("_")

            if (accion_principal == opcion_visualizar): # Si la accion_principal es igual a opcion_visualizar (las tuplas definidas anteriormente elegidas por el usuario)
                visualizar()
            elif (accion_principal == opcion_registrar):
                visualizar()
                registrar()
                visualizar()
            elif (accion_principal == opcion_modificar):
                visualizar()
                modificar()
                visualizar()
            elif (accion_principal == opcion_eliminar):
                visualizar()
                eliminar()
                visualizar()
            elif (accion_principal == opcion_buscar):
                buscar()

        accion = input('¿Desea iniciar otra acción? De ser así escriba "Iniciar" de lo contrario escribir "Fin": ')
    
    elif accion == "Fin" or accion == "fin" or accion == "FIN": # Si el valor de la variable accion es fin, finalice el programa.
        print("Programa finalizado.")
        break
    else: # Si el valor de la variable accion no es ni iniicar ni fin, finalice el programa.
        print("No ingreso un valor correcto.")
        print("Programa finalizado.")
        break