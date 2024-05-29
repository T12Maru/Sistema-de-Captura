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

# Explicación de la estructura del proyecto.

Al abrir el directorio Sistema-de-captura, nos podemos encontrar con el archivo **manage.py**, este archivo es relevante y no a la vez. Haciendo uso de este archivo podemos conectar todas las funcionalidades y herramientas que nos proporciona django, además que podremos ejecutar el proyecto, no deberá tocarse en casi ningun momento.      
Además de este archivo tendremos los 2 directorios siguientes:
- Sistema-de-captura: Contiene todos los archivos que realizan alguna configuración global en el proyecto. Se puede realizar la conexión con la base de datos, crear modelos abstractos, etc. Dentro de algunos archivos importantes, están:
  1. Setting.py Este archivo es el que nos permite configurar la base de datos, normalmente solo se modificará 1 vez en la creación del proyecto.
  2. urls.py Este archivo es el que nos permite crear urls permitidas en la página. Cada url tiene un "path" en la pagina, que corresponde a la dirección, una acción dentro del backend y un alías o nombre que permitira identificar esa url en el backend.
  3. _init _.py Este archivo permite ejecutar alguna librería o instrucción al momento de iniciar el servidor.
- Main: Contiene todos los archivos que corresponden a la interacción entre backend y frontend. Dentro es este directorio, contamos con 1 carpeta templates, además de los siguientes archivos importantes:
  1. admin.py Permite realizar ajustes en el "administrador" de django, este administrador es como una interfaz para administradores, se puede visualizar las bases de datos conectadas, además de crear nuevos elementos dentro de ellas.
  2. models.py Este archivo permite crear "modelos". Un modelo en django, sería lo correspondiente a una tabla. Dicho de otra forma, nos permite crear una base de datos, además esta misma puede contener ciertas funciones dentro de ella, debido a que los modelos son objetos.
  3. views.py Este archivo es el más importante del proyecto. Dentro de él nos encontramos con toda la lógica del programa, además de su aporte dinámico a la página. Dentro del archivo se encuentran funciones cuyo nombre corresponde a las urls permitidas en la página, cada vez que se solicita la entrada en una url, se ejecuta una de estas funciones, las cuales se encargar da enviar el archivo html correspondiente, además de un dato extra dependiendo de la solicitud.
  - Templates: Esta carpeta contiene todos los archivos que corresponden a la parte visual del programa. Entre ellos están:
    1. Grafico.html Este archivo es el encargado de solicitar datos de la base de datos, y posteriormente solicitar a highcharts que imprima una gráfica en la página.
    2. Inicio.html Se muestra el home del sistema.
    3. Plantilla.hhtml Este archivo contiene una plantilla, cómo es normal en las paginas como facebook o twitter, estas tienen una barra de navegación que se mantienen constantes, o existen ciertas paginas del gobierno, las cuales mantiene un mismo pie de página. Estos son elementos constantes, en la plantilla se agregan aquellos elementos que se mantiene invariables, y se deja una ubicación para que el programador pueda manipularlo a su manera.
    4. Signin.html Se encarga de mostrar un formulario, el cuál permite el inicio de sesion.
    5. Signup.html Se encarga de mostrar un formulario , el cuál permite el registro de un usuario.
  
   
# ¿Qué me encontraré dentro de la página?

Al correr el programa, se iniciara una pestaña con una barra de navegación que contiene los botones:
- Signin: Permite iniciar sesión con una cuenta previamente registrada.
- Signup: Permite registrar una cuenta nueva en la base de datos.
Si iniciamos sesión, nos aparecerá una nueva barra de navegación con los botones:
- Inicio: Te manda a la url que corresponde al inicio del sistema.
- Grafico: Te direcciona a una pagina que muestra graficas hacerca de los contagios por dengue en sonora/ciertos estados de méxico.
- Logout: Cierra la sesión de la cuenta actual.
