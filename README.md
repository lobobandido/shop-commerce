# shop-commerce
Proyecto de E-Commerce DreamSoft

Proyecto de E-Commerce con Django 



primera etapa 

contenido del repositorio+++++

configuración Proyecto base 
configuración de la base de datos
configuración de tablas  para categorías 
productos y creación del panel de control

Este proyecto es un e-commerce con los siguientes avances:  se creo un entorno virtual, se crean las dependencias,  conectamos la base de datos, creamos una app web, dentro de esta app web configuramos 2 modelos (categoría y productos) y por último se creo el panel de administración.

comandos :
python -m venv venv-----creamos entorno virtual

source venv/Scripts/activate------  activamos entorno virtual

django-admin startproject aarshop .   esto genera 2 carpetas (settings.py  urls.py ) y ya no crea otra carpeta con el punto agregado

python manage.py startapp web       (creamos nuestra app web)

python manage.py runserver           iniciamos nuestro server 

git status                           para ver cambios en nuestro proyecto 

git add .                            area de trabajo (cache de git)

git commit -m                        deja un comentrio en en el proyecto "proyecto inicial

git push origin main                 manda cambios al repositorio

python manage.py migrate

python manage.py makemigrations

python manage.py create superuser

https://pypi.org/project/django-admin-tailwind/  agregamos formato al panel de administración