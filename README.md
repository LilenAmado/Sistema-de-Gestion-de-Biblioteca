# Sistema-de-Gestion-de-Biblioteca
########################### Sistema de Gestión de Bibliotecas ###########################

    Objetivo: Desarrollar una solución de software para gestionar el préstamo y devolución de libros en una
    biblioteca.

    Realizado el análisis de requerimientos con el bibliotecario responsable se ha determinado necesario registrar
    los siguientes datos:

    Requerimientos:
        1. Registro de Libros:
            ● ID de Libro (número único y autoincremental)
            ● Título
            ● Autor
            ● Editorial
            ● Año de Publicación
            ● Género
            ● Cantidad Disponible
        2. Gestión de Socios:
            ● ID de Socio (número único y autoincremental)
            ● Nombre
            ● Apellido
            ● Fecha de Nacimiento
            ● Dirección
            ● Correo Electrónico
            ● Teléfono
        3. Registro de Préstamos y Devoluciones:
            ● ID de Préstamo (número único y autoincremental)
            ● ID de Socio
            ● ID de Libro
            ● Fecha de Préstamo
            ● Costo (en caso de que tuviera)
            ● Fecha de Devolución
            ● Estado del Préstamo (En Curso/Devuelto)

    Características del Software:
        ● Almacenamiento de Información: utilización de archivos JSON para almacenar los datos solicitados.
        ● Interfaces de usuario interactiva que permitan:
        ● Registrar, editar y eliminar libros.
        ● Registrar, editar y eliminar socios.
        ● Registrar préstamos y devoluciones.
        ● Búsqueda de libros por título, género, autor y editorial.
        ● Generar reportes de préstamos y devoluciones por socio, libro y rango de fechas.
        ● Por último, se deberá desarrollar una funcionalidad extra del software a criterio del alumno/grupo.
        Esta nueva funcionalidad puede incluir, como por ejemplo: desarrollo de interfaz gráfica, consumo de
        una api externa, búsquedas avanzadas, nuevas funcionalidades similares a las anteriores que aporten
        valor agregado, etc
