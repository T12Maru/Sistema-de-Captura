# Sistema-de-Captura

Este repositorio contiene los archivos necesarios para crear un sistema el cual permite el logup, login y logout de una página web. Además el sistema permite presentar una gráfica dinámica haciendo uso de la libreria highcharts en JavaScript.

## Objetivo del proyecto:

El objetivo principal del proyecto es aprender el cómo diferentes tecnologías interactuan entre ellas al momento de crear una página web. Siendo más especifico, se buscará la interacción entre la página web, el servidor y una base de datos.

## Herramientas tecnológicas que se utilizan en el proyecto:

- Para el diseño de la página web, se utilizó Django como framework de trabajo, debido a su gran versatilidad y gran apoyo de librerias para desarrollo web.
  - Para la parte visual se utilizó HTML y CSS/bootstrap.
  - Para la parte lógica y dinámica se utilizó JavaScript.  
- Como base de datos, se utilizará MySQL.
- Como libreria gráfica, si hizo uso de highcharts.
# Pasos para correr la página web en su propia computadora
1. Instalar Python y MySql (de preferencia) en su computadora.
2. Dentro de Python, asegurarse de tener instalada la librería pymysql y django, si no cuenta con ellas, deberá instalarlas. En windows se pueden instalar dichas librerias haciendo uso del CMD. Mediante el comando *pip install PyMySQL* se puede instalar pymysql. Y puede usar *pip install django* para instalar Django.
3. Haciendo uso de MySql, crear una base de datos de nombre **nombre_db** (puede usar el nombre a su gusto), asignarle un usuario y una contraseña con todos los permisos de manipulación.
4. Descargar este repositorio.
5. Dentro de la carpeta del proyecto "Sistema-de-captura", ubicar el archivo settings.py, este archivo contiene multiples configuraciones globales correspondientes al proyecto, de momento solo deberá modificar la configuración de la base de datos. Para esto vaya a la linea del codigo número 77, la cual dice "DATABASES".
6. Ingresar los datos correspondientes para realizar la conexión con su base de datos MySql.Si desea vincular otra base de datos distinta a MySql, deberá leer la documentación de django: [Ir a la documentación](https://docs.djangoproject.com/en/5.0/ref/databases/)      
En la configuración **ENGINE** deberá agregar la asociada a su base de datos, si esta usando MySql, el repositorio ya la tiene ingresada, en otro caso deberá consultar la documentación antes mencionada.     
Posteriormente aparece la configuración **NAME**, que se refiere al nombre de la base de datos a la cual buscará conectarse.    
Los demas elementos corresponden a el usuario y contraseña que haya proporcionado a la base de datos creada previamente.
8. Finalmente, usando la terminar, ubicarse en el directorio del proyecto donde se encuentra el archivo manage.py y ejecucar el comando python manage.py runserver. Si el comando no funciona, use el siguiente comando: py manage.py runserver.
9. Si python arroja un error, debe ser debido a que falta hacer las migraciones de la base de datos, para ello usaremos los siguientes comandos seguidos uno del otro:
   1. python manage.py makemigrations
   2. python manage.py migrate
10. Ejecutamos nuevamente el comando python manage.py runserver.
   
