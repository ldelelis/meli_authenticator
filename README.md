Autenticador Mercadolibre
=========================

`meli-auth` es un autenticador pensado para
integrarse facilmente con cualquier aplicación.

Expone una API RESTful fácil de usar, y una base
de datos MongoDB para resguardo e integridad
de los datos necesarios.

La aplicación también provee configuración de vistas,
para adaptar el look & feel a tus necesidades.

Instalación
-----------

El repositorio provee un servicio docker-compose,
para garantizar la portabilidad a cualquier servidor.

Alternativamente, los requerimientos para un deploy al
servidor estan provistos en `requirements.txt`

Desarrollo local
----------------

```bash
export FLASK_APP=meli_auth
export FLASK_ENV=development
flask run
```

Configuración
-------------

1. Definir una URL raiz (por defecto `/api/v1`).
En caso de requerir una distinta, modificar la
variable correspondiente en Dockerfile, y
en la configuración de `nginx`.
2. Agregar en `Dockerfile` el
CLIENT_ID y CLIENT_SECRET provistos por tu
aplicación.
3. Reemplazar `logo.png` en `meli_auth/static/images`
por un logo adecuado al sistema que se incluya.

Uso
---

* {root_url}: Index de la aplicación. Se le indica
al usuario a autenticarse en la aplicación con un
botón.
* {root_url/callback}: Callback post-autenticacion
con MercadoLibre. Se lo redirige automaticamente
al cliente para indicarle que se registró
correctamente en el sistema
* {root_url/\<id\>/token}: Vista API que devuelve el
token correspondiente a un ID de MercadoLibre, en
caso de estar registrado.
