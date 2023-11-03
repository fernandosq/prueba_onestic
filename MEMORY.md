# Introducción

Los primeros pasos que di para la prueba no fueron a nivel de código, lo primero que hice fue hacer un mapa conceptual con todo lo que había que desarrollar en la prueba, leí varias veces lo que se pedía, a continuación sobre papel y boli escribí las capas que iba a tener la API para así poder gestionar los csv`s iniciales y poder transformarlos en los reportes que se deben descargar.

# Decisiones tomadas

Valore varias opciones a la hora de realizar el procesarmiento de los csv`s:
* Python puro (sin librerias externas)
* Pandas
* Base de datos

Los motivos por los cuales tome la decisión de utilizar la base de datos son:

* En esta se utilizan ORM que es lo más afín para Django, tecnología requerida para el puesto de backend
* Al usar una base de datos se guarda el estado de los informes

## Estructura de codigo 

Como había que desarrollar una API y un comando que hicieran el mismo procesamiento de csv´s he creado el codigo de la manera más desacoplada posible.

# Proyecto

Se crea un virtual venv para instalar Django, y crear un proyecto el cual se le pone un nombre descriptivo acorde al ejercicio de la prueba, y dentro de este proyecto creamos una app que es la que va a gestionar los csv para generar con esos archivos los 3 reportes que se piden.

# Pasos seguidos

Una vez se ha creado la estructura básica del proyecto se crea un documento .gitignore para no subir al repositorio archivos innecesarios (alguno se me ha pasado aunque lo ido corrigiendo según lo veía), continuación he ido haciendo para cada desarrolló una rama diferente que luego han sido mergeadas en main, con sus correspondientes commits, aunque a la hora de hacer el pull request utilizaba el squash and merge de forma que queda más limpio para leer los commits, siempre poniendome como reviwer a mi mismo(esto en un entorno profesional pondría a algún compañero).



A continuación lo que hice fue crear los ORM de Django a través del model, estructurandolo en báse a las columnas de los diferentes csv,en este punto decidí utilizar para el "cost" un Decimal debido a que al leer la documentación Django vi que era más preciso, y al ser un tema de precios considere que es bastante importante que sea lo más preciso posible ese campo para que no haya desajustes en un futuro sobre cálculos con ese [campo](https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.FloatField).

Una vez desarrollados los Models empecé con la parte que iba a gestionar los csv iniciales, para guardarlos en base de datos y luego procesarlos, hice pequeñas funciones con sus tests con un setup previo, que comprueben que su funcionalidad básica es la correcta, respecto al precio tambíen ajuste que se redondeará a dos dígitos debido a que en los precios tenían hasta 10 decimales .
Luego desarrolle la parte en la cual se generan los reportes con sus columnas y nombre de csv que les corresponde acorde a lo que se pide en la prueba.

# API

Para la parte de hacer la aplicación una API por la descripción dudé si había que hacer un solo endpoint que recibiera los csv y en la respuesta los devolviera, pero considere una mejor opción dividirlo en dos endpoints individuales, uno para actualizar los csv iniciales, y otro que devuelva los reportes, en los endpoints utilice las funciones desarrolladas anteriormente, en el primer endpoint en el que se recibe los csv pues se guardan los datos de estos en la base de datos ayudándonos de ORM`s, y en el otro endpoint en el cual devolvemos con la respuesta los csv los envíe guardando estos en un zip que a su vez es guardado en una unidad de memoría que se envía para que el usuario pueda descargar el zip con los 3 reportes que se piden.
https://docs.djangoproject.com/en/4.2/ref/request-response/

# COMANDO

Para no hacer solo la API hice también esta parte que se pedía como requerimiento básico, ayudandome de parte de documentación debido a que no me acordaba de ciertas cosas como la estructura normativa en la cual guardar los commandos("https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html").Implementó el comando pasando la ruta de los archivos como argumento y creándose estos en el proyecto, añade un mensaje para saber si ha ido todo bien una vez ha sido lanzado el command.

# DOCKER

Para esta parte de docker utilice documentación oficial de docker, ya que había partes que no me acordaba como se hacían, añadí también un .dockerignore para todos esos archivos que no hace falta que sean copiados.Una vez se tiene el proyecto clonado desde github, estando en la raíz del proyecto donde está el Dockerfile se ejecuta el siguiente comando:

* `docker build -t acme_financial_tool .` 
* `docker run -p 8000:8000 -d acme_financial_tool` -> Habilitar siempre la ip localhost en el settings del proyecto 

De esta forma tenemos la aplicación operativa para poder hacer peticiones a los diferentes endpoints creados:

* upload/files/
* download/reports/