# megaproyecto

Manual de Instalación


El objetivo de este manual es guiar a futuros interesados en la instalación de la herramienta en Ubuntu 14.04 Linux.


Preparación del Ambiente.
Instalación de apache2
Ejecutar: sudo apt-get install apache2
Instalación de Mysql.
Ejecutar: sudo apt-get update
Ejecutar: sudo apt-get install mysql-server libmysqlclient-dev
Establecer un usuario y contraseña administrativa para MySQL.
Establecer el directorio de las bases de datos con el siguiente comando: sudo mysql_install_db
Instalación de los schemas de manera segura ejecutando: sudo mysql_secure_installation. (Seleccionar qué no a la primera pregunta, sí a todo lo demás).
Instalación de pip.
sudo apt-get install python-pip
Instalacion virtual env.
Ejecutar: sudo apt-get update
Ejecutar: sudo pip install virtualenv.
Copiar la carpeta del Git.
Acceder al repo.
Clonar el repo (https://github.com/cesaregm7/megaproyecto) y colocarlo en la carpeta /home/ubuntu.
Instalar requirements
Estando en la carpeta de Cipa, ingresar al ambiente virtual ejecutando : source CipaEnvirorment/bin/activate
Instalar requerimientos ejecutando: sudo pip install requirements
Para salir del ambiente virtual ejecutar: deactivate
Configuración de apache2.
Ingresar a etc/apache2/sites-available.
Modificar el 000-default-conf agregando al archivo lo siguiente inmediatamente antes de la línea que dice </VirtualHost> :
	*Ver archivo 000-default.conf en el git
Nota: Para este paso se asume que la carpeta del proyecto sí se encuentra pegada en /home/ubuntu
	c. Habilitar el servicio de la página ejecutando: sudo a2ensite 000-default.conf


Cargar el backup en la BD.
Abrir una terminal.
Ir al directorio del repositorio donde se encuentra el archivo sql (cipa.sql) que contiene el backup de la base de datos.
Acceder a la base de datos con el siguiente comando: mysql -u root -p
con la contraseña ‘toor’.
Crear la base de datos cipaDB con el siguiente comando: Create database cipaDB.
Seleccionar la base de datos a usar con el siguiente comando: use cipaDB;
Cargar la base de datos con el siguiente comando: \. Cipa.sql
Salirse de MySQL.
Crear un usuario para la administración de la base de datos cipaDB 
Abrir una shell de MySQL con el usuario y contraseña administrativa
Correr el siguiente comando para crear un nuevo usuario: CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
Asignar permisos sobre cipaDB al usuario recién creado al ejecutar: GRANT ALL PRIVILEGES ON cipaDB TO 'newuser'@'localhost';
Ejecutar el siguiente comando para recargar los privilegios: FLUSH PRIVILEGES;
Finalizar saliendo de la shell de MySQL con: EXIT;
Agregar el usuario con privilegios sobre la base de datos en la configuración de Django
 Acceder a cipa/settings.py
En la sección de bases de datos, cambiar los campos USER y PASSWORD a los campos correspondientes.
Cambiar los permisos de la carpeta static, media y  record_files a www-data.
Sudo chown -R www-data:www-data static.
Sudo chmod -R 775 static.
Sudo chown -R www-data:www-data media.
Sudo chmod -R 775 media.
Sudo chown -R www-data:www-data record_files.
Sudo chmod -R 775 record_files.
Reinciar Apache con el siguiente comando: sudo service apache2 restart.

ANEXO
Líneas a agregar en el paso 2b

	 Alias /static /home/ubuntu/Cipa/static
    	<Directory /home/ubuntu/Cipa/static>
        	Require all granted
   	</Directory>


         Alias /media /home/ubuntu/Cipa/media
        <Directory /home/ubuntu/Cipa/media>
                Require all granted
        </Directory>




        <Directory /home/ubuntu/Cipa/cipa>
        	<Files wsgi.py>
        	    Require all granted
	        </Files>
        </Directory>


    WSGIDaemonProcess Cipa python-path=/home/ubuntu/Cipa:/home/ubuntu/Cipa/CipaEnvironment/lib/python2.7/site-packages
    WSGIProcessGroup Cipa
    WSGIScriptAlias / /home/ubuntu/Cipa/cipa/wsgi.py


Credenciales de administrador para ingresar al sitio:
Usuario: admin
Contraseña: cipa1234
