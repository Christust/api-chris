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
El valor del parámetro de ruta item_id se pasará a su función como el argumento item_id.
Entonces, si ejecuta este ejemplo y va a http://127.0.0.1:8000/items/foo, verá una respuesta de:
```
{"item_id":"foo"}
```

## Parámetros de ruta con tipos
Puede declarar el tipo de un parámetro de ruta en la función, utilizando anotaciones de tipo estándar de Python:
```
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```
En este caso, item_id se declara como un int.

# Parámetros de consulta
Cuando declara otros parámetros de función que no forman parte de los parámetros de ruta, se interpretan automáticamente como parámetros de "consulta".
```
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```
La consulta es el conjunto de pares clave-valor que van después del ? en una URL, separados por &.
Por ejemplo, en la URL:
http://127.0.0.1:8000/items/?skip=0&limit=10
...los parámetros de consulta son:
- skip: con un valor de 0
- límite: con un valor de 10

Como son parte de la URL, son cadenas "naturalmente".
Pero cuando los declara con tipos de Python (en el ejemplo anterior, como int), se convierten a ese tipo y se validan contra él.

## Valores predeterminados
Como los parámetros de consulta no son una parte fija de una ruta, pueden ser opcionales y pueden tener valores predeterminados.
En el ejemplo anterior, tienen valores predeterminados de skip=0 y limit=10.
Entonces, yendo a la URL:
```
http://127.0.0.1:8000/items/
```
Sería lo mismo que ir a:
```
http://127.0.0.1:8000/items/?skip=0&limit=10

```

## Parámetros opcionales
Del mismo modo puedes declarar parámetros de query opcionales definiendo el valor por defecto como None:
```
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
```

## Parámetros de query requeridos
Cuando declaras un valor por defecto para los parámetros que no son de path (por ahora solo hemos visto parámetros de query), entonces no es requerido.
Si no quieres añadir un valor específico sino solo hacerlo opcional, pon el valor por defecto como None.
Pero cuando quieres hacer que un parámetro de query sea requerido, puedes simplemente no declararle un valor por defecto:
```
from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str, no_needy: str = "no needy value",optional: Optional[str] = None):
    if optional:
        return {"item_id": item_id, "needy": needy, "no_needy":no_needy, "optional":optional}
    return {"item_id": item_id, "needy": needy, "no_needy":no_needy}
```

# Cuerpos de solicitud
Cuando necesita enviar datos desde un cliente (digamos, un navegador) a su API, los envía como un cuerpo de solicitud.
Un cuerpo de solicitud son datos enviados por el cliente a su API. Un cuerpo de respuesta son los datos que tu API envía al cliente.
Su API casi siempre tiene que enviar un cuerpo de respuesta. Pero los clientes no necesariamente necesitan enviar cuerpos de solicitud todo el tiempo.
Para declarar un cuerpo de solicitud, utiliza modelos Pydantic con todo su poder y beneficios.

### Nota
Para enviar datos, debe usar uno de: POST (el más común), PUT, DELETE o PATCH.
El envío de un cuerpo con una solicitud GET tiene un comportamiento indefinido en las especificaciones, sin embargo, es compatible con FastAPI, solo para casos de uso muy complejo/extremo.

## Importar modelo base de Pydantic
Primero, necesita importar BaseModel desde pydantic:
```
from pydantic import BaseModel
```

## Crea tu modelo de datos
Luego, declara su modelo de datos como una clase que hereda de BaseModel.
Use tipos estándar de Python para todos los atributos:
```
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
```

Al igual que cuando se declaran parámetros de consulta, cuando un atributo del modelo tiene un valor predeterminado, no es obligatorio. De lo contrario, es obligatorio. Use None para que sea simplemente opcional.
Por ejemplo, este modelo anterior declara un "objeto" JSON (o dictado de Python) como:
```
{
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}
```

...como la descripción y el impuesto son opcionales (con un valor predeterminado de None), este "objeto" JSON también sería válido.
```
{
    "name": "Foo",
    "price": 45.2,
}
```

## Declararlo como un parámetro.
Para agregarlo a su operación de ruta, declárelo de la misma manera que declaró la ruta y los parámetros de consulta:
```
@app.post("/items/")
async def create_item(item: Item):
    return item
```
...y declara su tipo como el modelo que creaste, Item.

# Parámetros de consulta y validaciones de cadenas
FastAPI le permite declarar información adicional y validación para sus parámetros.
Tomemos esta aplicación como ejemplo:
```
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```
El parámetro de consulta q es de tipo Opcional[str] (o str | None en Python 3.10), eso significa que es de tipo str pero también podría ser None y, de hecho, el valor predeterminado es None, por lo que FastAPI sabrá que no es necesario.

## Validación adicional
Vamos a hacer cumplir que aunque q es opcional, siempre que se proporcione, su longitud no supere los 50 caracteres.

### Importa Query
Para lograr eso, primero importa Query desde fastapi:
```
from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

## Usar Query como valor predeterminado
Y ahora utilícelo como el valor predeterminado de su parámetro, estableciendo el parámetro max_length en 50:
```
async def read_items(q: Optional[str] = Query(None, max_length=50)):
```

Como tenemos que reemplazar el valor predeterminado None con Query(None), el primer parámetro de Query tiene el mismo propósito de definir ese valor predeterminado.
Asi que:
```
q: Optional[str] = Query(None)
```

...hace que el parámetro sea opcional, lo mismo que:
```
q: Optional[str] = None
```
Luego, podemos pasar más parámetros a Query. En este caso, el parámetro max_length que se aplica a las cadenas:
```
q: str = Query(None, max_length=50)
```

Esto validará los datos, mostrará un error claro cuando los datos no sean válidos y documentará el parámetro en la operación de ruta de esquema de OpenAPI.

## Que sea requerida
Cuando no necesitamos declarar más validaciones o metadatos, podemos hacer que el parámetro de consulta q sea requerido simplemente no declarando un valor predeterminado, como:
```
q: str
```
en vez de:
```
q: Optional[str] = None
```
Pero ahora lo estamos declarando con Query, por ejemplo como:
```
q: Optional[str] = Query(None, min_length=3)
```
Entonces, cuando necesite declarar un valor como requerido mientras usa Query, puede usar ... como el primer argumento:
```
@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

## Lista de parámetros de consulta/valores múltiples
Cuando define un parámetro de consulta explícitamente con Query, también puede declararlo para recibir una lista de valores, o dicho de otra manera, para recibir múltiples valores.
Por ejemplo, para declarar un parámetro de consulta q que puede aparecer varias veces en la URL, puede escribir:
```
@app.get("/items/")
async def read_items(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items
```
Luego, con una URL como:
```
http://localhost:8000/items/?q=foo&q=bar
```

# Parámetros de ruta y validaciones numéricas
De la misma manera que puede declarar más validaciones y metadatos para parámetros de consulta con Query, puede declarar el mismo tipo de validaciones y metadatos para parámetros de ruta con Path.

## Importar Path
```
from fastapi import FastAPI, Path, Query
```