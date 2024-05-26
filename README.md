# Sistema-de-Captura
Este repositorio contiene los archivos necesarios para crear un sistema el cual permite la captura de los requisitos que tienen las personas que solicitan un apoyo alimentario.  El sistema trabaja con 2 niveles de permisos, están los permisos tipo usuario, y los permisos tipo administrador.
## Objetivo del proyecto:
El objetivo principal del proyecto es otorgar un apoyo al Banco de Alimentos, eficientando la captura de información a los trabajadores sociales, quienes tienen como tarea principal realizar evaluaciones a las personas que solicitan un apoyo alimentario. A estas personas se les realizan una serie de preguntas, cuyas respuestas permiten llenar un formulario.
El sistema buscara que por medio de un usuario/administrador, se puedan ingresar los datos del formulario a una base de datos, y posteriormente facilitar el manejo de la información.
## Características del sistema:
- Crear un sistema de inicio/salida de sesión (login/logout).
- Crear múltiples herramientas para que un Administrador pueda modificar/consultar la base de datos que corresponde a los usuarios creados.
- Crear múltiples herramientas para que tanto usuarios como administradores puedan consultar/modificar la base de datos que corresponde a alimentos almacenados en el Banco de Alimentos.
## Herramientas tecnológicas que se utilizarán en el proyecto:
- Se hará uso de Django como framework de trabajo, debido a su gran versatilidad y gran apoyo de librerias para desarrollo web.
- Para la parte visual se utilizará HTML y CSS.
- Se utilizó JavaScript para utilidades dinámicas en la página. 
- Como base de datos, se utilizará MySQL.

#Pasos para correr la página web en su propia computadora
1. Instalar Python y MySql en su computadora.
2. Dentro de Python, asegurarse de tener instalada la librería pymysql y django, si no cuenta con ellas, deberá instalarlas. En windows se puede usar el comando pip install PyMySQL para instalar pymysql. Y puede usar pip install django para instalar Django.
3. Haciendo uso de MySql, crear una base de datos llamada usuarios, asignarle un usuario y una contraseña.
4. Descargar el repositorio.
5. Dentro de la carpeta del proyecto "BancoAlimentos", ubicar el archivo settings.py, este archivo contiene multiples configuraciones correspondientes al proyecto, de momento solo deberá modificar la configuración de la base de datos. Para esto vaya a la linea del codigo número 77, la cual dice "DATABASES".
6. Ingresar los datos correspondientes para realizar la conexión con su base de datos MySql. Si desea vincular otra base de datos distinta a MySql, deberá leer la documentación de django.
7. Finalmente, usando la terminar, ubicarse en el directorio del proyecto donde se encuentra el archivo manage.py y ejecucar el comando python manage.py runserver. Si el comando no funciona, use el siguiente comando: py manage.py runserver.
8. Si python arroja un error, debe ser debido a que falta hacer las migraciones de la base de datos, para ello usaremos los siguientes comandos seguidos uno del otro:
  i. python manage.py makemigrations
  ii. python manage.py migrate
9. Ejecutamos nuevamente el comando python manage.py runserver.
   
