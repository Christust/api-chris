# FastAPI
## Tutorial - Guía del usuario - Introducción
Este tutorial le muestra cómo usar FastAPI con la mayoría de sus funciones, paso a paso.
Cada sección se basa gradualmente en las anteriores, pero está estructurada en temas separados, de modo que puede ir directamente a cualquier tema específico para resolver sus necesidades específicas de API.
También está diseñado para funcionar como una referencia futura.
Para que pueda volver y ver exactamente lo que necesita.

## Ejecutar el código
Todos los bloques de código se pueden copiar y usar directamente (en realidad son archivos Python probados).
Para ejecutar cualquiera de los ejemplos, copie el código en un archivo main.py e inicie uvicorn con:
```
uvicorn main:app --reload
```
Se recomienda **ENCARECIDAMENTE** que escriba o copie el código, lo edite y lo ejecute localmente.

Usarlo en tu editor es lo que realmente te muestra los beneficios de FastAPI, ver el poco código que tienes que escribir, todas las verificaciones de tipo, el autocompletado, etc.

## Instalar FastAPI
El primer paso es instalar FastAPI.
Para el tutorial, es posible que desee instalarlo con todas las dependencias y características opcionales:
```
pip install "fastapi[all]"
```
...que también incluye uvicorn, que puedes usar como el servidor que ejecuta tu código.

# Primeros pasos
El archivo FastAPI más simple podría verse así:
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```
Copie eso en un archivo `main.py`.
Ejecute el servidor en vivo:
```
uvicorn main:app --reloadEl comando uvicorn main:app se refiere a:

main: el archivo main.py (el "módulo" de Python).
app: el objeto creado dentro de main.py con la línea app = FastAPI().
--reload: hace que el servidor se reinicie después de cambios en el código. Uso exclusivo para desarrollo.
```

### Nota
El comando `uvicorn main:app --reload` se refiere a:

- main: el archivo main.py (el "módulo" de Python).
- app: el objeto creado dentro de main.py con la línea app = FastAPI().
- --reload: hace que el servidor se reinicie después de cambios en el código. Uso exclusivo para desarrollo.

En la salida, hay una línea con algo como:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Esa línea muestra la URL donde se sirve su aplicación, en su máquina local.

## Revisalo
Abra su navegador en http://127.0.0.1:8000
Verá la respuesta JSON como:
```
{"message": "Hello World"}
```

## Documentos de API interactivos
Ahora ve a http://127.0.0.1:8000/docs
Verá la documentación de la API interactiva automática (proporcionada por la interfaz de usuario de Swagger)

## Documentos API alternativos
Y ahora, vaya a http://127.0.0.1:8000/redoc
Verá la documentación automática alternativa (proporcionada por ReDoc)

## OpenAPI
FastAPI genera un "esquema" con toda su API utilizando el estándar OpenAPI para definir las API.

### **Esquema**
Un "esquema" es una definición o descripción de algo. No el código que lo implementa, sino solo una descripción abstracta.

### **Esquema API**
En este caso, OpenAPI es una especificación que dicta cómo definir un esquema de su API.
Esta definición de esquema incluye sus rutas de API, los posibles parámetros que toman, etc.

### **Esquema de datos**
El término "esquema" también puede referirse a la forma de algunos datos, como un contenido JSON.
En ese caso, significaría los atributos JSON y los tipos de datos que tienen, etc.

### **Esquema OpenAPI y JSON**
OpenAPI define un esquema de API para su API. Y ese esquema incluye definiciones (o "esquemas") de los datos enviados y recibidos por su API usando JSON Schema, el estándar para esquemas de datos JSON.

### **Compruebe el archivo openapi.json**
Si tiene curiosidad acerca de cómo se ve el esquema de OpenAPI sin procesar, FastAPI genera automáticamente un JSON (esquema) con las descripciones de todas sus API.
Puede verlo directamente en: http://127.0.0.1:8000/openapi.json.
Mostrará un JSON que comienza con algo como:
```
{
    "openapi": "3.0.2",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items/": {
            "get": {
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
.
.
.
```

### **Para qué sirve OpenAPI**
El esquema OpenAPI es lo que impulsa los dos sistemas de documentación interactivos incluidos.
Y hay decenas de alternativas, todas basadas en OpenAPI. Puede agregar fácilmente cualquiera de esas alternativas a su aplicación creada con FastAPI.
También puede usarlo para generar código automáticamente, para clientes que se comunican con su API. Por ejemplo, aplicaciones frontend, móviles o IoT.

## Resumen, paso a paso
### Paso 1: Importar FastAPI
```
from fastapi import FastAPI
```
FastAPI es una clase de Python que proporciona toda la funcionalidad para su API.

### Paso 2: Crea una "instancia" de FastAPI
```
app = FastAPI()
```
Aquí, la variable de la aplicación será una "instancia" de la clase FastAPI.
Este será el principal punto de interacción para crear toda su API.

### Paso 3: Crear una operación de ruta
#### **Ruta**
"Ruta" aquí se refiere a la última parte de la URL a partir de la primera /
Entonces, en una URL como:
```
https://example.com/items/foo
```
...la ruta seria:
```
/items/foo
```
Al crear una API, la "ruta" es la forma principal de separar "inquietudes" y "recursos".

#### **Operación**
"Operación" aquí se refiere a uno de los "métodos" HTTP.
Uno de:
- POST
- GET
- PUT
- DELETE

... Y los más exóticos:
- OPTIONS
- HEAD
- PATCH
- TRACE

En el protocolo HTTP, puede comunicarse con cada ruta usando uno (o más) de estos "métodos".
Al crear API, normalmente utiliza estos métodos HTTP específicos para realizar una acción específica.
Normalmente usas:
- POST: para crear datos.
- GET: para leer datos.
- PUT: para actualizar datos.
- DELETE: para borrar datos.

OpenAPI, cada uno de los métodos HTTP se denomina "operación".
También las llamaremos "operaciones".

#### **Definir un decorador de operación de ruta**
```
@app.get("/")
```
`@app.get("/")` le dice a FastAPI que la función justo debajo está a cargo de manejar las solicitudes que van a:
- La ruta /
- Utilizando una operación de GET

También puede utilizar las otras operaciones:
- @app.post()
- @app.put()
- @app.delete()

Y las más exóticas:
- @app.options()
- @app.head()
- @app.patch()
- @app.trace()

### Paso 4: Definir la función de operación de ruta
Esta es nuestra "función de operación de ruta":

- Ruta: es /.
- Operación: es GET.
- Función: es la función debajo del "decorador" (debajo de @app.get("/")).

```
async def root():
```
Esta es una función de Python.
FastAPI lo llamará cada vez que reciba una solicitud a la URL "/" mediante una operación GET.
En este caso, es una función asíncrona.

### Paso 5: Devolver el contenido
```
return {"message": "Hello World"}
```
Puede devolver un diccionario, una lista, valores singulares como str, int, etc.
También puede devolver modelos de Pydantic (verá más sobre eso más adelante).
Hay muchos otros objetos y modelos que se convertirán automáticamente a JSON (incluidos ORM, etc.). Intente usar sus favoritos, es muy probable que ya sean compatibles.

# Parámetros de ruta
Puede declarar la ruta "parámetros" o "variables" con la misma sintaxis utilizada por las cadenas de formato de Python:
```
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```
<<<<<<< HEAD
El valor del parámetro de ruta item_id se pasará a su función como el argumento item_id.
Entonces, si ejecuta este ejemplo y va a http://127.0.0.1:8000/items/foo, verá una respuesta de:
```
{"item_id":"foo"}
```

# Parámetros de ruta con tipos
Puede declarar el tipo de un parámetro de ruta en la función, utilizando anotaciones de tipo estándar de Python:
```
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```
En este caso, item_id se declara como un int.
=======
>>>>>>> 3a44777f098465679249ab2b48d905407e52502b
