-------------------------------------

 DESCRIPCION

	Este proyecto, creado a partir de un framework llamado Django, 
	es una página web que representa una academia de boxeo.
	La misma cumple diversas funcionalidades como:

	- Un usuario NO registrado (o visitante) podrá:
		.- Registrarse como Usuario
		.- Ingresar al "Home" (Inicio)
		.- Ingresar al "About" (Sobre Mí)
		.- Revisar y realizar busquedas especificas en el
			listado de árbitros, boxeadores y entrenadores
	
	- Un usuario registrado podrá:
		.- Registrarse como árbitro, boxeador y/o entrenador
			.- Editar su información de árbitro, boxeador y/o
				entrenador
			.- Borrar su registro de árbitro, boxeador y/o
				entrenador
		
		.- Editar su información de su cuenta de Usuario
		.- Eliminar su cuenta de Usuario, que, a su vez,
			borraría toda información enlazada a la misma
			 (registros de árbitro, boxeador y/o entrenador)

	- Un superusuario (Admin) podrá:
		.- Desde la página:
			.- Editar y/o Eliminar, cualquier registro de
				cualquier usuario

		.- Desde el panel:
			.- Editar y/o Eliminar cualquier Usuario
			.- Editar y/o Eliminar cualquier registro de
				cualquier Usuario
			
-------------------------------------

 INSTALACION

	PASO 0
		--- DESCARGAR EL REPOSITORIO ---
		1.- Crear una carpeta raíz/base/madre
		2.- Clonar el repositorio con el siguiente comando:
			
			$ git clone [link del repositorio]

	PASO 1
		--- DESCARGAR LAS DEPENDENCIAS ---
		1.- Ubicarse en la carpeta que contiene el archivo "requeriments.txt"
		2.- Instalar las dependencias con el siguiente comando:
			
			$ pip install -r requeriments.txt

	PASO 2
		--- INICIAR SERVIDOR ---
		1.- Ubicarse en la carpeta que contiene el archivo "manage.py"
		2.- Iniciar el servidor con el siguiente comando:
			
			$ python manage.py runserver

-------------------------------------