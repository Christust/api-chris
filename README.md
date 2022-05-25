# Tutorial - Guía del usuario - Introducción
Este tutorial te muestra cómo usar FastAPI con la mayoría de sus características paso a paso.
Cada sección se basa gradualmente en las anteriores, pero está estructurada en temas separados, así puedes ir directamente a cualquier tema en concreto para resolver tus necesidades específicas sobre la API.
Funciona también como una referencia futura, para que puedas volver y ver exactamente lo que necesitas.

## Ejecuta el código
Todos los bloques de código se pueden copiar y usar directamente (en realidad son archivos Python probados).
Para ejecutar cualquiera de los ejemplos, copia el código en un archivo llamado main.py, y ejecuta uvicorn de la siguiente manera en tu terminal:
```
uvicorn main:app --reload
```
Se recomienda **ENCARECIDAMENTE** que escriba o copie el código, lo edite y lo ejecute localmente.
Usarlo en tu editor de código es lo que realmente te muestra los beneficios de FastAPI, al ver la poca cantidad de código que tienes que escribir, todas las verificaciones de tipo, autocompletado, etc.

## Instala FastAPI
El primer paso es instalar FastAPI.
Para el tutorial, es posible que quieras instalarlo con todas las dependencias y características opcionales:
```
pip install "fastapi[all]"
```
...eso también incluye uvicorn que puedes usar como el servidor que ejecuta tu código.

## Guía Avanzada de Usuario
También hay una Guía Avanzada de Usuario que puedes leer luego de este Tutorial - Guía de Usuario.
La Guía Avanzada de Usuario, se basa en este tutorial, utiliza los mismos conceptos y enseña algunas características adicionales.
Pero primero deberías leer el Tutorial - Guía de Usuario (lo que estas leyendo ahora mismo).
La guía esa diseñada para que puedas crear una aplicación completa con solo el Tutorial - Guía de Usuario, y luego extenderlo de diferentes maneras, según tus necesidades, utilizando algunas de las ideas adicionales de la Guía Avanzada de Usuario.

# Primeros pasos
Un archivo muy simple de FastAPI podría verse así:

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
uvicorn main:app --reload
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
Abra su navegador en `http://127.0.0.1:8000`
Verá la respuesta JSON como:

```
{"message": "Hello World"}
```

## Documentos de API interactivos
Ahora ve a `http://127.0.0.1:8000/docs`
Verá la documentación de la API interactiva automática (proporcionada por la interfaz de usuario de Swagger)

## Documentos API alternativos
Y ahora, vaya a `http://127.0.0.1:8000/redoc`
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
Puede verlo directamente en: `http://127.0.0.1:8000/openapi.json`.
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

### Paso 3: Crear una operación **path**
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

#### **Definir un decorador de operación **path****
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

### Paso 4: Definir la función de operación **path**
Esta es nuestra "función de operación **path**":

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

# Parámetros de path
Puedes declarar los "parámetros" o "variables" con la misma sintaxis que usan los format strings de Python:
```
from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```

El valor del parámetro de path item_id será pasado a tu función como el argumento item_id.
Entonces, si corres este ejemplo y vas a `http://127.0.0.1:8000/items/foo`, verás una respuesta de:
```
{"item_id":"foo"}
```

## Parámetros de path con tipos
Puedes declarar el tipo de un parámetro de path en la función usando las anotaciones de tipos estándar de Python:
```
from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```
En este caso, item_id es declarado como un int.

## Conversión de datos
Si corres este ejemplo y abres tu navegador en `http://127.0.0.1:8000/items/3` verás una respuesta de:
```
{"item_id":3}
```

## Validación de datos
Pero si abres tu navegador en `http://127.0.0.1:8000/items/foo` verás este lindo error de HTTP:
```
{
    "detail": [
        {
            "loc": [
                "path",
                "item_id"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}
```
debido a que el parámetro de path item_id tenía el valor "foo", que no es un int.

El mismo error aparecería si pasaras un float en vez de un int como en: `http://127.0.0.1:8000/items/4.2`

## Pydantic
Toda la validación de datos es realizada tras bastidores por Pydantic, así que obtienes todos sus beneficios. Así sabes que estás en buenas manos.
Puedes usar las mismas declaraciones de tipos con str, float, bool y otros tipos de datos más complejos.
Exploraremos varios de estos tipos en los próximos capítulos del tutorial.

## El orden importa
Cuando creas operaciones de path puedes encontrarte con situaciones en las que tengas un path fijo.
Digamos algo como /users/me que sea para obtener datos del usuario actual.
... y luego puedes tener el path /users/{user_id} para obtener los datos sobre un usuario específico asociados a un ID de usuario.
Porque las operaciones de path son evaluadas en orden, tienes que asegurarte de que el path para /users/me sea declarado antes que el path para /users/{user_id}:
```
from fastapi import FastAPI
app = FastAPI()

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
```

De otra manera el path para /users/{user_id} coincidiría también con /users/me "pensando" que está recibiendo el parámetro user_id con el valor "me".

## Valores predefinidos
Si tienes una operación de path que recibe un parámetro de path pero quieres que los valores posibles del parámetro de path sean predefinidos puedes usar un Enum estándar de Python.

### Crea una clase `Enum`
Importa Enum y crea una sub-clase que herede desde str y desde Enum.
Al heredar desde str la documentación de la API podrá saber que los valores deben ser de tipo string y podrá mostrarlos correctamente.
Luego crea atributos de clase con valores fijos, que serán los valores disponibles válidos:
```
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

```

### Declara un parámetro de path
Luego, crea un parámetro de path con anotaciones de tipos usando la clase enum que creaste (ModelName):
```
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

### Revisa la documentación
Debido a que los valores disponibles para el parámetro de path están predefinidos, la documentación interactiva los puede mostrar bien.

### Trabajando con los enumerations de Python
El valor del parámetro de path será un enumeration member.

#### Compara enumeration members
Puedes compararlo con el enumeration member en el enum (ModelName) que creaste:
```
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}
```

#### Obtén el enumeration value
Puedes obtener el valor exacto (un str en este caso) usando model_name.value, o en general, your_enum_member.value:
```
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}
```

#### Devuelve enumeration members
Puedes devolver enum members desde tu operación de path inclusive en un body de JSON anidado (por ejemplo, un dict).
Ellos serán convertidos a sus valores correspondientes (strings en este caso) antes de devolverlos al cliente:
```
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}
```

En tu cliente obtendrás una respuesta en JSON como:
```
{
  "model_name": "alexnet",
  "message": "Deep Learning FTW!"
}
```

### Parámetros de path parameters que contienen paths
Digamos que tienes una operación de path con un path /files/{file_path}.
Pero necesitas que el mismo file_path contenga un path como home/johndoe/myfile.txt.
Entonces, la URL para ese archivo sería algo como: /files/home/johndoe/myfile.txt.

#### Soporte de OpenAPI
OpenAPI no soporta una manera de declarar un parámetro de path que contenga un path, dado que esto podría llevar a escenarios que son difíciles de probar y definir.
Sin embargo, lo puedes hacer en FastAPI usando una de las herramientas internas de Starlette.
La documentación seguirá funcionando, aunque no añadirá ninguna información diciendo que el parámetro debería contener un path.

#### Convertidor de path
Usando una opción directamente desde Starlette puedes declarar un parámetro de path que contenga un path usando una URL como:
```
/files/{file_path:path}
```

En este caso el nombre del parámetro es file_path y la última parte, :path, le dice que el parámetro debería coincidir con cualquier path.
Entonces lo puedes usar con:
```
from fastapi import FastAPI
app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
```

# Parámetros de query
Cuando declaras otros parámetros de la función que no hacen parte de los parámetros de path estos se interpretan automáticamente como parámetros de "query".
```
from fastapi import FastAPI
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```

El query es el conjunto de pares de key-value que van después del ? en la URL, separados por caracteres &.
Por ejemplo, en la URL:
```
http://127.0.0.1:8000/items/?skip=0&limit=10
```
...los parámetros **query** son:
- skip: con un valor de 0
- límite: con un valor de 10

Dado que son parte de la URL son strings "naturalmente".
Pero cuando los declaras con tipos de Python (en el ejemplo arriba, como int) son convertidos a ese tipo y son validados con él.
Todo el proceso que aplicaba a los parámetros de path también aplica a los parámetros de query:
- Soporte del editor (obviamente)
- "Parsing" de datos
- Validación de datos
- Documentación automática

## Configuraciones por defecto
Como los parámetros de query no están fijos en una parte del path pueden ser opcionales y pueden tener valores por defecto.
El ejemplo arriba tiene skip=0 y limit=10 como los valores por defecto.
Entonces, si vas a la URL:
```
http://127.0.0.1:8000/items/
```

Sería lo mismo que ir a:
```
http://127.0.0.1:8000/items/?skip=0&limit=10
```

Pero, si por ejemplo vas a:
```
http://127.0.0.1:8000/items/?skip=20

```

Los valores de los parámetros en tu función serán:

- skip=20: porque lo definiste en la URL
- limit=10: porque era el valor por defecto

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

En este caso el parámetro de la función q será opcional y será None por defecto.

## Conversión de tipos de parámetros de query
También puedes declarar tipos bool y serán convertidos:
```
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
```

En este caso, si vas a:
```
http://127.0.0.1:8000/items/foo?short=1
```

o:
```
http://127.0.0.1:8000/items/foo?short=True
```

o:
```
http://127.0.0.1:8000/items/foo?short=true
```

o:
```
http://127.0.0.1:8000/items/foo?short=on
```

o:
```
http://127.0.0.1:8000/items/foo?short=yes
```

o cualquier otra variación (mayúsculas, primera letra en mayúscula, etc.) tu función verá el parámetro short con un valor bool de True. Si no, lo verá como False.

## Múltiples parámetros de path y query
Puedes declarar múltiples parámetros de path y parámetros de query al mismo tiempo. FastAPI sabe cuál es cuál.
No los tienes que declarar en un orden específico.
Serán detectados por nombre:
```
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
```

## Parámetros de query requeridos
Cuando declaras un valor por defecto para los parámetros que no son de path (por ahora solo hemos visto parámetros de query), entonces no es requerido.
Si no quieres añadir un valor específico sino solo hacerlo opcional, pon el valor por defecto como None.
Pero cuando quieres hacer que un parámetro de query sea requerido, puedes simplemente no declararle un valor por defecto:
```
http://127.0.0.1:8000/items/foo-item
```

...sin añadir el parámetro needy requerido, verás un error como:
```
{
    "detail": [
        {
            "loc": [
                "query",
                "needy"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
}
```

Dado que needy es un parámetro requerido necesitarías declararlo en la URL:
```
http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
```

...esto funcionaría:
```
{
    "item_id": "foo-item",
    "needy": "sooooneedy"
}
```

Por supuesto que también puedes definir algunos parámetros como requeridos, con un valor por defecto y otros completamente opcionales:
```
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
```

En este caso hay 3 parámetros de query:

- needy, un str requerido.
- skip, un int con un valor por defecto de 0.
- limit, un int opcional.

# Request Body
Cuando necesita enviar datos desde un cliente (digamos, un navegador) a su API, los envía como un **request body**.
Un **request body** son datos enviados por el cliente a su API. Un **response body** son los datos que tu API envía al cliente.
Su API casi siempre tiene que enviar un **response body**. Pero los clientes no necesariamente necesitan enviar **request body** todo el tiempo.
Para declarar un **request body**, utiliza modelos Pydantic con todo su poder y beneficios.

### Nota
Para enviar datos, debe usar uno de: POST (el más común), PUT, DELETE o PATCH.
El envío de un **request body** GET tiene un comportamiento indefinido en las especificaciones, sin embargo, es compatible con FastAPI, solo para casos de uso muy complejo/extremo.
Como se desaconseja, los documentos interactivos con la interfaz de usuario de Swagger no mostrarán la documentación del cuerpo al usar GET, y es posible que los proxies intermedios no lo admitan.

## Importar BaseModel de Pydantic
Primero, necesita importar `BaseModel` desde pydantic:
```
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
```

## Crea tu modelo de datos
Luego, declara su modelo de datos como una clase que hereda de BaseModel.
Use tipos estándar de Python para todos los atributos:
```
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
```

Al igual que cuando se declaran parámetros de query, cuando un atributo del modelo tiene un valor predeterminado, no es obligatorio. De lo contrario, es obligatorio. Use `None` para que sea simplemente opcional.
Por ejemplo, este modelo anterior declara un "`objet`" JSON (o `dict` de Python) como:
```
{
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}
```

...como la `description` y `tax` son opcionales (con un valor predeterminado de None), este "`objet`" JSON también sería válido.
```
{
    "name": "Foo",
    "price": 45.2,
}
```

## Declararlo como un parámetro.
Para agregarlo a su operación **path**, declárelo de la misma manera que declaró la ruta y los parámetros **query**:
```
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
```
...y declara su tipo como el modelo que creaste, `Item`.

## Usa el modelo
Dentro de la función, puede acceder directamente a todos los atributos del objeto modelo:
```
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
```

## Request Body + Parametros Path
Puede declarar los parámetros de **path** y el **body request** al mismo tiempo.
FastAPI reconocerá que los parámetros de la función que coinciden con los parámetros de **path** deben tomarse de la ruta, y que los parámetros de la función que se declaran como modelos de Pydantic deben tomarse del **body request**.
```
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
```

## Request Body + Parametros Path + Parametros Query
También puede declarar **body**, **path** y parámetros **query**, todo al mismo tiempo.
FastAPI reconocerá cada uno de ellos y tomará los datos del lugar correcto.
```
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
```

Los parámetros de la función se reconocerán de la siguiente manera:
- Si el parámetro también se declara en la ruta, se utilizará como parámetro **path**.
- Si el parámetro es de un tipo singular (como int, float, str, bool, etc.) se interpretará como un parámetro **query**.
- Si se declara que el parámetro es del tipo de un modelo Pydantic, se interpretará como un **body request**.

# Parámetros **query** y validaciones de cadenas
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
El parámetro **query** `q` es de tipo `Opcional[str]` (o `str | None` en Python 3.10), eso significa que es de tipo `str` pero también podría ser `None` y, de hecho, el valor predeterminado es `None`, por lo que FastAPI sabrá que no es necesario.

## Validación adicional
Vamos a hacer cumplir que aunque `q` es opcional, siempre que se proporcione, su longitud no supere los 50 caracteres.

### Importa Query
Para lograr eso, primero importa `Query` desde fastapi:
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

## Usar `Query` como valor predeterminado
Y ahora utilícelo como el valor predeterminado de su parámetro, estableciendo el parámetro `max_length` en 50:
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

Como tenemos que reemplazar el valor predeterminado `None` con `Query(None)`, el primer parámetro de Query tiene el mismo propósito de definir ese valor predeterminado.
Asi que:
```
q: Optional[str] = Query(None)
```

...hace que el parámetro sea opcional, lo mismo que:
```
q: Optional[str] = None
```

Y en Python 3.10 y superior:
```
q: str | None = Query(None)
```

...hace que el parámetro sea opcional, lo mismo que:
```
q: str | None = None
```

Pero lo declara explícitamente como un parámetro **query**.

Tenga en cuenta que la parte más importante para hacer que un parámetro sea opcional es la parte:
```
= None
```

o el:
```
= Query(None)
```

ya que usará `None` como el valor predeterminado, y de esa manera hará que el parámetro no sea necesario.
La parte `Optional` le permite a su editor brindar un mejor soporte, pero no es lo que le dice a FastAPI que este parámetro no es necesario.

Luego, podemos pasar más parámetros a `Query`. En este caso, el parámetro `max_length` que se aplica a las cadenas:
```
q: str = Query(None, max_length=50)
```

Esto validará los datos, mostrará un error claro cuando los datos no sean válidos y documentará el parámetro en la operación **path** de esquema de OpenAPI.

## Agrega mas validaciones
También puede agregar un parámetro `min_length`:
```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: str | None = Query(None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

## Agregar expresiones regulares
Puede definir una expresión regular que el parámetro debe coincidir:
```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: str | None = Query(None, min_length=3, max_length=50, regex="^fixedquery$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

Esta expresión regular específica comprueba que el valor del parámetro recibido:
- ^: comienza con los siguientes caracteres, no tiene caracteres anteriores.
- fixedquery: tiene el valor exacto fixedquery.
- $: termina ahí, no tiene más caracteres después de fixedquery.

Si te sientes perdido con todas estas ideas de "expresiones regulares", no te preocupes. Son un tema difícil para muchas personas. Todavía puedes hacer muchas cosas sin necesidad de expresiones regulares todavía.
Pero siempre que los necesite e ir a aprenderlos, sepa que ya puede usarlos directamente en FastAPI.

## Valores predeterminados
De la misma manera que puede pasar `None` como el primer argumento que se utilizará como valor predeterminado, puede pasar otros valores.
Digamos que desea declarar el parámetro **query** `q` para que tenga una longitud mínima de 3 y un valor predeterminado de "`fixedquery`":
```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: str = Query("fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

## Que sea requerida
Cuando no necesitamos declarar más validaciones o metadatos, podemos hacer que el parámetro **query** `q` sea requerido simplemente no declarando un valor predeterminado, como:
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
Entonces, cuando necesite declarar un valor como requerido mientras usa `Query`, puede usar `...` como el primer argumento:
```
@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

Esto le permitirá a FastAPI saber que este parámetro es obligatorio.

## Lista de parámetros **query**/valores múltiples
Cuando define un parámetro **query** explícitamente con Query, también puede declararlo para recibir una lista de valores, o dicho de otra manera, para recibir múltiples valores.
Por ejemplo, para declarar un parámetro **query** `q` que puede aparecer varias veces en la URL, puede escribir:
```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: list[str] | None = Query(None)):
    query_items = {"q": q}
    return query_items
```

Luego, con una URL como:
```
http://localhost:8000/items/?q=foo&q=bar
```

recibiría los valores de los múltiples parámetros **query** q (foo y bar) en una lista de Python dentro de su función de operación **path**, en el parámetro de función q.
Entonces, la respuesta a esa URL sería:
```
{
  "q": [
    "foo",
    "bar"
  ]
}
```

### Lista de parámetros **query**/valores múltiples con valores predeterminados
Y también puede definir una lista predeterminada de valores si no se proporciona ninguno:
```
from typing import List
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items
```

Si vas a:
```
http://localhost:8000/items/
```

el valor predeterminado de q será: ["foo", "bar"] y su respuesta será:
```
{
  "q": [
    "foo",
    "bar"
  ]
}
```

#### Usando `list`
También puede usar list directamente en lugar de `List[str]` (o `list[str]` en Python 3.9+):
```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: list = Query([])):
    query_items = {"q": q}
    return query_items
```

Tenga en cuenta que, en este caso, FastAPI no verificará el contenido de la lista.
Por ejemplo, `List[int]` comprobaría (y documentaría) que el contenido de la lista son números enteros. Pero la lista por sí sola no lo haría.


## Declarar más metadatos
Puede agregar más información sobre el parámetro.
Esa información se incluirá en la OpenAPI generada y será utilizada por las interfaces de usuario de la documentación y las herramientas externas.

### Puedes agregar un titulo:
```
from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(None, title="Query string", min_length=3)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

### Y una descripción:
```
from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

## Alias parameters
Imagine que quiere que el parámetro sea `item-query`.
Como en:
```
http://127.0.0.1:8000/items/?item-query=foobaritems
```

Pero `item-query` no es un nombre de variable de Python válido.
El más cercano sería `item_query`.
Pero aún necesita que sea exactamente un `item-query` ...
Entonces puede declarar un alias, y ese alias es lo que se usará para encontrar el valor del parámetro:
```
from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

## Parámetros obsoletos
Ahora digamos que ya no te gusta este parámetro.
Tienes que dejarlo allí por un tiempo porque hay clientes que lo usan, pero quieres que los documentos lo muestren claramente como obsoleto.
Entonces pase el parámetro deprecated=True a Query:
```
from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

## Excluir de OpenAPI
Para excluir un parámetro **query** del esquema OpenAPI generado (y, por lo tanto, de los sistemas de documentación automática), establezca el parámetro `include_in_schema` de `Query` en `False`:
```
from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    hidden_query: Optional[str] = Query(None, include_in_schema=False)
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
```

# Parámetros **path** y validaciones numéricas
De la misma manera que puede declarar más validaciones y metadatos para parámetros **query** con `Query`, puede declarar el mismo tipo de validaciones y metadatos para parámetros **path** con Path.

## Importar Path
```
from typing import Optional
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

## Declare metadata
Puede declarar todos los mismos parámetros que para Query.
Por ejemplo, para declarar un valor de metadatos de título para el parámetro **path** item_id, puede escribir:
```
from typing import Optional
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

Siempre se requiere un parámetro **path**, ya que tiene que ser parte de la ruta.
Por lo tanto, debe declararlo con `...` para marcarlo como requerido.
Sin embargo, incluso si lo declaró con `None` o establecer un valor predeterminado, no afectaría nada, seguiría siendo siempre obligatorio.

## Ordena los parámetros como necesites
Digamos que desea declarar el parámetro **query** `q` como un `str` obligatorio.
Y no necesita declarar nada más para ese parámetro, por lo que realmente no necesita usar `Query`.
Pero aún necesita usar `Path` para el parámetro **path** `item_id`.
Python se quejará si coloca un valor con un "default" antes de un valor que no tiene un "default".
Pero puede reordenarlos y tener el valor sin un valor predeterminado (el parámetro **query** q) primero.
No importa para FastAPI. Detectará los parámetros por sus nombres, tipos y declaraciones predeterminadas (`Query`, `Path`, etc.), no le importa el orden.
Entonces, puedes declarar tu función como:
```
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    q: str, item_id: int = Path(..., title="The ID of the item to get")
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

## Ordena los parámetros como necesites, trucos
Si desea declarar el parámetro **query** `q` sin `Query` ni ningún valor predeterminado, y el parámetro **path** `item_id` usando `Path`, y tenerlos en un orden diferente, Python tiene una pequeña sintaxis especial para eso.
Pasar *, como primer parámetro de la función.
Python no hará nada con ese *, pero sabrá que todos los siguientes parámetros deben llamarse como argumentos de palabras clave (key-value pairs), también conocidos como kwargs. Incluso si no tienen un valor predeterminado.
```
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get"), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

## Validaciones de números: mayor o igual
Con `Query` y `Path` (y otros que verá más adelante) puede declarar restricciones de cadenas, pero también restricciones de números.
Aquí, con `ge=1`, `item_id` deberá ser un número entero "mayor o igual (greater than or equal)" a 1.
```
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get", ge=1), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

## Validaciones de números: mayor que y menor que o igual
Lo mismo aplica para:

- gt: mayor que (greater than)
- le: menor o igual (less than or equal)
```
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get", ge=1), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

## Validaciones de números: flotantes, mayor que y menor que
Las validaciones de números también funcionan para valores `float`.
Aquí es donde se vuelve importante poder declarar `gt` y no solo `ge`. Al igual que con él, puede exigir, por ejemplo, que un valor sea mayor que 0, incluso si es menor que 1.
Entonces, 0.5 sería un valor válido. Pero 0.0 o 0 no lo harían.
Y lo mismo para el `lt`.
```
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(..., gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

## Recapitalución
Con `Query`, `Path` (y otras que aún no ha visto) puede declarar metadatos y validaciones de cadenas de la misma manera que con Parámetros de `query` y Validaciones de cadenas.
Y también puedes declarar validaciones numéricas:
- gt: greater than
- ge: greater than or equal
- lt: less than
- le: less than or equal

Query, Path y otras que verá más adelante son subclases de una clase Param común (que no necesita usar).
Y todos ellos comparten los mismos parámetros de validación y metadatos adicionales que ha visto.

Cuando importa Query, Path y otros desde fastapi, en realidad son funciones.
Que cuando se le llame, devuelva instancias de clases del mismo nombre.
Entonces, importa Query, que es una función. Y cuando lo llama, devuelve una instancia de una clase también llamada Query.
Estas funciones están ahí (en lugar de solo usar las clases directamente) para que su editor no marque errores sobre sus tipos.
De esa manera, puede usar su editor normal y sus herramientas de codificación sin tener que agregar configuraciones personalizadas para ignorar esos errores.

# Body - Multiples Parametros
Ahora que hemos visto cómo usar Path y Query, veamos usos más avanzados de las declaraciones del **Request Body**.

## Combina parámetros Path, Query y Body
En primer lugar, por supuesto, puede mezclar declaraciones de parámetros `Path`, `Query` y **Request Body** libremente y FastAPI sabrá qué hacer.
Y también puede declarar los **body request** como opcionales, configurando el valor predeterminado en `None`:
```
from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: Optional[str] = None,
    item: Optional[Item] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results
```

Tenga en cuenta que, en este caso, el elemento que se tomaría del cuerpo es opcional. Como tiene un valor predeterminado None.

## Múltiples parametros Body
En el ejemplo anterior, las operaciones **path** esperarían un cuerpo JSON con los atributos de un elemento, como:
```
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
```

Pero también puede declarar múltiples parámetros **body**, ej. `item` y `user`:
```
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    username: str
    full_name: Optional[str] = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results
```

En este caso, FastAPI notará que hay más de un **body parameters** en la función (dos parámetros que son modelos de Pydantic).
Entonces, usará los nombres de los parámetros como claves (nombres de campo) en el cuerpo y esperará un cuerpo como:
```
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
```

Tenga en cuenta que aunque el elemento se declaró de la misma manera que antes, ahora se espera que esté dentro del cuerpo con un elemento clave.
FastAPI hará la conversión automática de la solicitud, de modo que el parámetro `item` reciba su contenido específico y lo mismo para `user`.
Realizará la validación de los datos compuestos y los documentará así para el esquema OpenAPI y los documentos automáticos.

## Valores singulares en el **body**
De la misma manera que hay `Query` y `Path` para definir datos adicionales para los parámetros de consulta y ruta, FastAPI proporciona un `Body` equivalente.
Por ejemplo, ampliando el modelo anterior, podría decidir que quiere tener otra clave `importance` en el mismo cuerpo, además de `item` y el `user`.
Si lo declara tal cual, porque es un valor singular, FastAPI asumirá que es un parámetro de consulta.
Pero puede indicarle a FastAPI que lo trate como otra clave de cuerpo usando Body:
```
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    username: str
    full_name: Optional[str] = None

@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: int = Body(...)
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results
```

En este caso, FastAPI esperará un **body** como:
```
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
```

Nuevamente, convertirá los tipos de datos, validará, documentará, etc.

## Múltiples parámetros **body** y **query**
Por supuesto, también puede declarar parámetros **query** adicionales cuando lo necesite, además de cualquier parámetro **body**.
Como, de forma predeterminada, los valores singulares se interpretan como parámetros **query**, no tiene que agregar explícitamente un `Query`, solo puede hacer lo siguiente:
```
q: Optional[str] = None
```

O en Python 3.10 y superior:
```
q: str | None = None
```

Por ejemplo:
```
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    username: str
    full_name: Optional[str] = None

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(..., gt=0),
    q: Optional[str] = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results
```

Body también tiene los mismos parámetros adicionales de metadatos y validación que Query, Path y otros que verá más adelante.

## Incustrar un solo parámetro **body**
Supongamos que solo tiene un parámetro **body** `item` único de un modelo Pydantic `Item`.
De forma predeterminada, FastAPI esperará su **body** directamente.
Pero si desea que espere un JSON con una clave `item` y dentro de él el contenido del modelo, como lo hace cuando declara parámetros de cuerpo adicionales, puede usar el parámetro `Body` especial `embed`:
```
item: Item = Body(..., embed=True)
```

como en:
```
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
```

En este caso, FastAPI esperará un cuerpo como:
```
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
```

en vez de:
```
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
```

## Resumen
Puede agregar varios parámetros **body** a su función de operación **path**, aunque una solicitud solo puede tener un **body**.
Pero FastAPI lo manejará, le brindará los datos correctos en su función y validará y documentará el esquema correcto en la operación **path**.
También puede declarar valores singulares para que se reciban como parte del **body**.
Y puede indicarle a FastAPI que incruste **body** en una clave incluso cuando solo se haya declarado un parámetro.

# Body - Fields
De la misma manera que puede declarar validación y metadatos adicionales en los parámetros de la función de operación **path** con Query, Path y Body, puede declarar la validación y los metadatos dentro de los modelos de Pydantic usando Field de Pydantic.

## Importar Field
Primero, tienes que importarlo:
```
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
```

Tenga en cuenta que Field se importa directamente desde pydantic, no desde fastapi como todos los demás (Consulta, Ruta, Cuerpo, etc.).

## Declarar atributos del modelo
Luego puede usar Field con atributos de modelo:
```
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
```

Field funciona de la misma manera que Query, Path y Body, tiene todos los mismos parámetros, etc.
En realidad, Query, Path y otros que verá a continuación crean objetos de subclases de una clase Param común, que es en sí misma una subclase de la clase FieldInfo de Pydantic.
Y Field también devuelve una instancia de FieldInfo.
Body también devuelve objetos de una subclase de FieldInfo directamente. Y hay otras que verás más adelante que son subclases de la clase Body.
Recuerde que cuando importa Query, Path y otras desde fastapi, en realidad son funciones que devuelven clases especiales.
Observe cómo el atributo de cada modelo con un tipo, valor predeterminado y Field tiene la misma estructura que el parámetro de una función de operación **path**, con Field en lugar Path, Query y Body.

## Añadir información adicional
Puede declarar información adicional en Field, Query, Body, etc. Y se incluirá en el Esquema JSON generado.
Aprenderá más sobre cómo agregar información adicional más adelante en los documentos, cuando aprenda a declarar ejemplos.
Las claves adicionales pasadas a Field también estarán presentes en el esquema OpenAPI resultante para su aplicación. Como es posible que estas claves no formen parte necesariamente de la especificación de OpenAPI, es posible que algunas herramientas de OpenAPI, por ejemplo, el validador de OpenAPI, no funcionen con su esquema generado.

## Resumen
Puede usar el campo de Pydantic para declarar validaciones y metadatos adicionales para los atributos del modelo.
También puede usar los argumentos de palabras clave adicionales para pasar metadatos de esquema JSON adicionales.

# Body - Modelos anidados
Con FastAPI, puede definir, validar, documentar y usar modelos arbitrariamente anidados (gracias a Pydantic).

## Campos de lista
Puede definir un atributo para que sea un subtipo. Por ejemplo, un `list` de Python:
```
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: list = []

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

Esto hará que `tags` sean una lista de elementos. Aunque no declara el tipo de cada uno de los elementos.

## Campos `List` con  tipo de parámetro
Pero Python tiene una forma específica de declarar listas con tipos internos o "parámetros de tipo":

### Importar `List` de `typing`
En Python 3.9 y superior, puede usar la lista estándar para declarar estas anotaciones de tipo, como veremos a continuación.
Pero en las versiones de Python anteriores a la 3.9 (3.6 y superiores), primero debe importar List desde el módulo `typing` estándar de Python:
```
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

### Declarar `list` con un parámetro de tipo
Para declarar tipos que tienen parámetros de tipo (tipos internos), como `list`, `dict`, `tuple`:
- Si tiene una versión de Python anterior a la 3.9, importe su versión equivalente desde el módulo de escritura
- Pase los tipos internos como "parámetros de tipo" utilizando corchetes: [ y ]

En Python 3.9 sería:
```
my_list: list[str]
```

En versiones de Python anteriores a la 3.9, sería:
```
from typing import List

my_list: List[str]
```

Esa es toda la sintaxis estándar de Python para declaraciones de tipos.
Utilice esa misma sintaxis estándar para los atributos del modelo con tipos internos.
Entonces, en nuestro ejemplo, podemos hacer que `tags` sean específicamente una "lista de cadenas":
```
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

## Tipos `Set`
Pero luego lo pensamos y nos damos cuenta de que las etiquetas no deberían repetirse, probablemente serían cadenas únicas.
Y Python tiene un tipo de datos especial para conjuntos de elementos únicos, `set`.
Entonces podemos declarar `tags` como un conjunto de cadenas:
```
from typing import Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

Con esto, incluso si recibe una solicitud con datos duplicados, se convertirá en un conjunto de elementos únicos.
Y cada vez que genere esos datos, incluso si la fuente tuviera duplicados, se generará como un conjunto de elementos únicos.
Y también se anotará / documentará en consecuencia.

## Modelos anidados
Cada atributo de un modelo Pydantic tiene un tipo.
Pero ese tipo puede ser en sí mismo otro modelo Pydantic.
Por lo tanto, puede declarar "objetos" JSON profundamente anidados con nombres, tipos y validaciones de atributos específicos.
Todo eso, arbitrariamente anidado.

### Define un submodelo
Por ejemplo, podemos definir un modelo `Image`:
```
from typing import Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[Image] = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

### Usar el submodelo como un tipo
Y luego podemos usarlo como el tipo de un atributo:
```
from typing import Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[Image] = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

Esto significaría que FastAPI esperaría un cuerpo similar a:
```
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    }
}
```

Nuevamente, haciendo solo esa declaración, con FastAPI obtienes:
- Compatibilidad con el editor (finalización, etc.), incluso para modelos anidados
- Conversión de datos
- Validación de datos
- Documentación automática

## Tipos especiales y validación
Aparte de los tipos singulares normales como str, int, float, etc. Puede usar tipos singulares más complejos que heredan de str.
Para ver todas las opciones que tiene, consulte los documentos de los tipos exóticos de Pydantic. Verá algunos ejemplos en el próximo capítulo.
Por ejemplo, como en el modelo `Image` tenemos un campo de `url`, podemos declararlo en lugar de `str`, `HttpUrl` de Pydantic:
```
from typing import Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[Image] = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

Se comprobará que la cadena sea una URL válida y se documentará en JSON Schema/OpenAPI como tal.

## Atributos con listas de submodelos
También puede usar modelos Pydantic como subtipos de `list`, `set`, etc.:
```
from typing import List, Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    images: Optional[List[Image]] = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

Esto esperará (convertir, validar, documentar, etc.) un cuerpo JSON como:
```
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": [
        "rock",
        "metal",
        "bar"
    ],
    "images": [
        {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        },
        {
            "url": "http://example.com/dave.jpg",
            "name": "The Baz"
        }
    ]
}
```

Observe cómo la clave de `images` ahora tiene una `list` de objetos `Image`.

## Modelos profundamente anidados
Puede definir arbitrariamente modelos profundamente anidados:
```
from typing import List, Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    images: Optional[List[Image]] = None

class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer
```

Observe cómo `Offer` tiene una lista de `Item`s, que a su vez tienen una lista opcional de `Image`s

## Cuerpos de listas puras
Si el valor de nivel superior del cuerpo JSON que espera es una matriz JSON (una lista de Python), puede declarar el tipo en el parámetro de la función, al igual que en los modelos de Pydantic:
```
images: List[Image]
```

o en Python 3.9 y superior:
```
images: List[Image]
```

como en:
```
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images
```

## Soporte para editores en todas partes
Y obtienes soporte de editor en todas partes.
No podría obtener este tipo de soporte de editor si estuviera trabajando directamente con dict en lugar de modelos Pydantic.
Pero tampoco tiene que preocuparse por ellos, los dictados entrantes se convierten automáticamente y su salida también se convierte automáticamente a JSON.

## Cuerpos de `dict`s arbitrarios
También puede declarar un cuerpo como `dict` con claves de algún tipo y valores de otro tipo.
Sin tener que saber de antemano cuáles son los nombres de campo/atributo válidos (como sería el caso de los modelos de Pydantic).
Esto sería útil si desea recibir claves que aún no conoce.
Otro caso útil es cuando desea tener claves de otro tipo, eje. `int`.
Eso es lo que vamos a ver aquí.
En este caso, aceptaría cualquier `dict` siempre que tenga claves `int` con valores `float`:
```
from typing import Dict
from fastapi import FastAPI

app = FastAPI()

@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights
```

Tenga en cuenta que JSON solo admite str como claves.
Pero Pydantic tiene conversión automática de datos.
Esto significa que, aunque sus clientes API solo pueden enviar cadenas como claves, siempre que esas cadenas contengan números enteros puros, Pydantic las convertirá y las validará.
Y el dict que recibe como pesos en realidad tendrá claves int y valores flotantes.

## Resumen
Con FastAPI tiene la máxima flexibilidad que brindan los modelos de Pydantic, mientras mantiene su código simple, corto y elegante.
Pero con todos los beneficios:
- Compatibilidad con el editor (¡completado en todas partes!)
- Conversión de datos (también conocido como análisis/serialización)
- Validación de datos
- Documentación del esquema
- Documentos automáticos

# Declarar solicitud de datos de ejemplo
Puede declarar ejemplos de los datos que su aplicación puede recibir.
Aquí hay varias maneras de hacerlo.

## Pydantic `schema_extra`
Puede declarar un ejemplo para un modelo Pydantic usando Config y schema_extra, como se describe en los documentos de Pydantic: Personalización del esquema:
```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

Esa información adicional se agregará tal cual al esquema JSON de salida para ese modelo, y se usará en los documentos de la API.

## Argumentos adicionales `Field`
Al usar `Field()` con modelos Pydantic, también puede declarar información adicional para el esquema JSON pasando cualquier otro argumento arbitrario a la función.
Puede usar esto para agregar un ejemplo para cada campo:
```
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(example="Foo")
    description: str | None = Field(default=None, example="A very nice Item")
    price: float = Field(example=35.4)
    tax: float | None = Field(default=None, example=3.2)

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

Tenga en cuenta que esos argumentos adicionales pasados ​​no agregarán ninguna validación, solo información adicional, con fines de documentación.

## `example` y `examples` en OpenAPI
Al usar cualquiera de:

- Sendero()
- Consulta()
- Encabezamiento()
- Galleta()
- Cuerpo()
- Forma()
- Archivo()

también puede declarar un `expample` de datos o un grupo de `expamples` con información adicional que se agregará a OpenAPI.

## Body con example
Aquí pasamos un `expample` de los datos esperados en `Body()`:
```
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(
        example={
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results
```

## Body con múltiples ejemplos
Alternativamente al `example` único, puede pasar `examples` usando un `dict` con múltiples ejemplos, cada uno con información adicional que también se agregará a OpenAPI.
Las claves del `dict` identifican cada ejemplo, y cada valor es otro `dict`.
Cada `dict` de ejemplo específico en los `examples` puede contener:
- summary: Breve descripción del ejemplo.
- description: una descripción larga que puede contener texto Markdown.
- value: Este es el ejemplo real que se muestra, p. un dictado
- externalValue: alternativa al valor, una URL que apunta al ejemplo. Aunque es posible que esto no sea compatible con tantas herramientas como value.
```
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item = Body(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results
```

# Tipos de datos adicionales
Hasta ahora, ha estado usando tipos de datos comunes, como:
- int
- float
- str
- bool

Pero también puede usar tipos de datos más complejos.
Y seguirás teniendo las mismas características que has visto hasta ahora:
- Gran apoyo del editor.
- Conversión de datos de solicitudes entrantes.
- Conversión de datos para datos de respuesta.
- Validación de datos.
- Anotación y documentación automática.

## Otros tipos de datos
Estos son algunos de los tipos de datos adicionales que puede usar:
- UUID:
- - Un "Identificador único universal" estándar, común como ID en muchas bases de datos y sistemas.
- - En solicitudes y respuestas se representará como una str.
- datetime.datetime:
- - Un archivo datetime.datetime de Python.
- - Las solicitudes y respuestas se representarán como una cadena en formato ISO 8601, como: 2008-09-15T15:53:00+05:00.
- datetime.date:
- - Python fechahora.fecha.
- - En las solicitudes y respuestas se representará como una cadena en formato ISO 8601, como: 2008-09-15.
- datetime.time:
- - Una fecha y hora de Python.
- - En las solicitudes y respuestas se representará como una cadena en formato ISO 8601, como: 14:23:55.003.
- datetime.timedelta:
- - Un archivo datetime.timedelta de Python.
- - En las solicitudes y respuestas se representará como un flotante de segundos totales.
- - Pydantic también permite representarlo como una "codificación de diferencia de tiempo ISO 8601", consulte los documentos para obtener más información.
- frozenset:
- - En solicitudes y respuestas, tratadas igual que un conjunto:
- - En las solicitudes se leerá un listado, eliminando los duplicados y convirtiéndolo en un conjunto.
- - En las respuestas, el conjunto se convertirá en una lista.
- - El esquema generado especificará que los valores establecidos son únicos (usando los elementos únicos del esquema JSON).
- bytes:
- - Bytes estándar de Python.
- - En solicitudes y respuestas serán tratadas como str.
- - El esquema generado especificará que es una cadena con "formato" binario.
- Decimal:
- - Decimal estándar de Python.
- - En solicitudes y respuestas, se maneja igual que un flotante.
- Puede verificar todos los tipos de datos pydantic válidos aquí: Tipos de datos pydantic.

## Ejemplo
Aquí hay una operación **path** de ejemplo con parámetros que usan algunos de los tipos anteriores.
```
from datetime import datetime, time, timedelta
from typing import Union
from uuid import UUID
from fastapi import Body, FastAPI

app = FastAPI()

@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Union[datetime, None] = Body(default=None),
    end_datetime: Union[datetime, None] = Body(default=None),
    repeat_at: Union[time, None] = Body(default=None),
    process_after: Union[timedelta, None] = Body(default=None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }
```

Tenga en cuenta que los parámetros dentro de la función tienen su tipo de datos natural y puede, por ejemplo, realizar manipulaciones de fechas normales, como:
```
from datetime import datetime, time, timedelta
from typing import Union
from uuid import UUID
from fastapi import Body, FastAPI

app = FastAPI()

@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Union[datetime, None] = Body(default=None),
    end_datetime: Union[datetime, None] = Body(default=None),
    repeat_at: Union[time, None] = Body(default=None),
    process_after: Union[timedelta, None] = Body(default=None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }
```

# Modelo de respuesta
Puede declarar el modelo utilizado para la respuesta con el parámetro response_model en cualquiera de las operaciones **path**:

- @aplicación.get()
- @aplicación.post()
- @aplicación.put()
- @aplicación.delete()
- etc.
```
from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item
```

Tenga en cuenta que el modelo de respuesta es un parámetro del método "decorador" (obtener, publicar, etc.). No de su función de operación de ruta, como todos los parámetros y el cuerpo.

Recibe el mismo tipo que declararía para un atributo de modelo Pydantic, por lo que puede ser un modelo Pydantic, pero también puede ser, p. una lista de modelos Pydantic, como List[Item].

FastAPI utilizará este modelo de respuesta para:
- Convierta los datos de salida a su declaración de tipo.
- Validar los datos.
- Agregue un esquema JSON para la respuesta, en la operación de ruta de OpenAPI.
- Será utilizado por los sistemas automáticos de documentación.

Pero lo mas importante:
- Limitará los datos de salida a los del modelo. Veremos cómo eso es importante a continuación.

El modelo de respuesta se declara en este parámetro en lugar de como una anotación de tipo de retorno de función, porque es posible que la función de ruta en realidad no devuelva ese modelo de respuesta, sino que devuelva un dictado, un objeto de base de datos o algún otro modelo, y luego use el modelo de respuesta para realizar el campo. limitación y serialización.

## Devolver los mismos datos de entrada
Aquí estamos declarando un modelo **UserIn**, contendrá una contraseña de texto sin formato:
```
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None

# Don't do this in production!
@app.post("/user/", response_model=UserIn)
async def create_user(user: UserIn):
    return user
```

Y estamos usando este modelo para declarar nuestra entrada y el mismo modelo para declarar nuestra salida:
```
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None

# Don't do this in production!
@app.post("/user/", response_model=UserIn)
async def create_user(user: UserIn):
    return user
```

Ahora, cada vez que un navegador crea un usuario con una contraseña, la API devolverá la misma contraseña en la respuesta.
En este caso, puede que no sea un problema, porque el propio usuario está enviando la contraseña.
Pero si usamos el mismo modelo para otra operación de ruta, podríamos estar enviando las contraseñas de nuestros usuarios a cada cliente.

Nunca almacene la contraseña simple de un usuario ni la envíe en una respuesta.

## Agregar un modelo de salida
En su lugar, podemos crear un modelo de entrada con la contraseña de texto sin formato y un modelo de salida sin ella:
```
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user
```

Aquí, aunque nuestra función de operación de ruta devuelve el mismo usuario de entrada que contiene la contraseña:
```
    return user
```

... declaramos que el `response_model` es nuestro modelo `UserOut`, que no incluye la contraseña:
```
@app.post("/user/", response_model=UserOut)
```

Entonces, FastAPI se encargará de filtrar todos los datos que no estén declarados en el modelo de salida (usando Pydantic).

## Parámetros de codificación del modelo de respuesta
Su modelo de respuesta podría tener valores predeterminados, como:
```
from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
```

- `description: Union[str, None] = None` tiene un valor predeterminado de None.
- `tax: float = 10.5` tiene un valor predeterminado de 10.5.
- `tags: List[str] = []` tiene como valor predeterminado de una lista vacía: [].

pero es posible que desee omitirlos del resultado si no se almacenaron realmente.

Por ejemplo, si tiene modelos con muchos atributos opcionales en una base de datos NoSQL, pero no desea enviar respuestas JSON muy largas llenas de valores predeterminados.

## Utilice el parámetro response_model_exclude_unset
Puede configurar el parámetro decorador de la operación de ruta de acceso response_model_exclude_unset=True:
```
from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
```
y esos valores predeterminados no se incluirán en la respuesta, solo los valores realmente establecidos.

Entonces, si envía una solicitud a esa operación de ruta para el elemento con ID foo, la respuesta (sin incluir los valores predeterminados) será:
```
{
    "name": "Foo",
    "price": 50.2
}
```

FastAPI usa .dict() del modelo Pydantic con su parámetro include_unset para lograr esto.
También puedes usar:
- response_model_exclude_defaults=True
- response_model_exclude_none=True

como se describe en los documentos de Pydantic para include_defaults y exclude_none.

### Datos con valores para campos con valores predeterminados
Pero si sus datos tienen valores para los campos del modelo con valores predeterminados, como el elemento con la barra de identificación:
```
{
    "name": "Bar",
    "description": "The bartenders",
    "price": 62,
    "tax": 20.2
}
```

Ellos serán incluidos en la respuesta.

### Datos con los mismos valores que los predeterminados
Si los datos tienen los mismos valores que los predeterminados, como el elemento con ID baz:
```
{
    "name": "Baz",
    "description": None,
    "price": 50.2,
    "tax": 10.5,
    "tags": []
}
```

FastAPI es lo suficientemente inteligente (en realidad, Pydantic es lo suficientemente inteligente) para darse cuenta de que, aunque la descripción, el impuesto y las etiquetas tienen los mismos valores que los valores predeterminados, se establecieron explícitamente (en lugar de tomarlos de los valores predeterminados).

Por lo tanto, se incluirán en la respuesta JSON.

### `response_model_include` y `response_model_exclude`
También puede utilizar los parámetros del decorador de la operación de ruta de acceso response_model_include y response_model_exclude.
Toman un conjunto de str con el nombre de los atributos a incluir (omitiendo el resto) o a excluir (incluyendo el resto).
Esto se puede usar como un atajo rápido si solo tiene un modelo de Pydantic y desea eliminar algunos datos de la salida.

Pero aún se recomienda usar las ideas anteriores, usando varias clases, en lugar de estos parámetros.
Esto se debe a que el esquema JSON generado en OpenAPI de su aplicación (y los documentos) seguirá siendo el del modelo completo, incluso si usa response_model_include o response_model_exclude para omitir algunos atributos.
Esto también se aplica a response_model_by_alias que funciona de manera similar.

```
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}

@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]

@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]
```

### Uso de `list` en lugar de `set`
Si olvida usar un `set` y usa una `list` o una `tuple` en su lugar, FastAPI aún lo convertirá en un `set` y funcionará correctamente:
```
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}

@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include=["name", "description"],
)
async def read_item_name(item_id: str):
    return items[item_id]

@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude=["tax"])
async def read_item_public_data(item_id: str):
    return items[item_id]
```

## Resumen
Utilice el parámetro del decorador de la operación de ruta para definir modelos de respuesta y, especialmente, para garantizar que se filtren los datos privados.
Use response_model_exclude_unset para devolver solo los valores establecidos explícitamente.

# Modelos adicionales
Siguiendo con el ejemplo anterior, será habitual tener más de un modelo relacionado.
Este es especialmente el caso de los modelos de usuario, porque:
- El modelo de entrada debe poder tener una contraseña.
- El modelo de salida no debe tener una contraseña.
- El modelo de base de datos probablemente necesitaría tener una contraseña cifrada.

Nunca almacene las contraseñas de texto sin formato del usuario. Almacene siempre un "hash seguro" que luego pueda verificar.
Si no lo sabe, aprenderá qué es un "hash de contraseña" en los capítulos de seguridad.

## Múltiples modelos
Aquí hay una idea general de cómo se verían los modelos con sus campos de contraseña y los lugares donde se usan:
```
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None

class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: Union[str, None] = None

def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db

@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved
```

## Sobre `**user_in.dict()`
### `.dict()` de Pydantic
user_in es un modelo Pydantic de la clase UserIn.
Los modelos Pydantic tienen un método .dict() que devuelve un dict con los datos del modelo.
Entonces, si creamos un objeto Pydantic user_in como:
```
user_in = UserIn(username="john", password="secret", email="john.doe@example.com")
```

y despues llamamos:
```
user_dict = user_in.dict()
```

ahora tenemos un dict con los datos en la variable user_dict (es un dict en lugar de un objeto de modelo Pydantic).
Y si llamamos:
```
print(user_dict)
```

obtendríamos un dictado de Python con:
```
{
    'username': 'john',
    'password': 'secret',
    'email': 'john.doe@example.com',
    'full_name': None,
}
```

### Desenvolviendo un dict
Si tomamos un dict como user_dict y lo pasamos a una función (o clase) con **user_dict, Python lo "desenvolverá". Pasará las claves y los valores de user_dict directamente como argumentos clave-valor.
Entonces, continuando con el user_dict de arriba, escribiendo:
```
UserInDB(**user_dict)
```

Daría como resultado algo equivalente a:
```
UserInDB(
    username="john",
    password="secret",
    email="john.doe@example.com",
    full_name=None,
)
```

O más exactamente, usando user_dict directamente, con cualquier contenido que pueda tener en el futuro:
```
UserInDB(
    username = user_dict["username"],
    password = user_dict["password"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
)
```

### Un modelo Pydantic a partir del contenido de otro
Como en el ejemplo anterior, obtuvimos user_dict de user_in.dict(), este código:
```
user_dict = user_in.dict()
UserInDB(**user_dict)
```

sería equivalente a:
```
UserInDB(**user_in.dict())
```

... porque user_in.dict() es un dict, y luego hacemos que Python lo "desenvuelva" pasándolo a UserInDB con **.
Entonces, obtenemos un modelo Pydantic de los datos en otro modelo Pydantic

### Desempaquetar un dictado y palabras clave adicionales
Y luego agregar el argumento de palabra clave adicional hash_password=hashed_password, como en:
```
UserInDB(**user_in.dict(), hashed_password=hashed_password)
```

... termina siendo como:
```
UserInDB(
    username = user_dict["username"],
    password = user_dict["password"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
    hashed_password = hashed_password,
)
```

Las funciones adicionales de soporte son solo para demostrar un posible flujo de datos, pero, por supuesto, no brindan ninguna seguridad real.

## Reducir la duplicación
Reducir la duplicación de código es una de las ideas centrales de FastAPI.
A medida que la duplicación de código aumenta las posibilidades de errores, problemas de seguridad, problemas de desincronización de código (cuando actualiza en un lugar pero no en los demás), etc.
Y todos estos modelos comparten una gran cantidad de datos y duplican nombres y tipos de atributos.
Podríamos hacerlo mejor.
Podemos declarar un modelo UserBase que sirva como base para nuestros otros modelos. Y luego podemos hacer subclases de ese modelo que heredan sus atributos (declaraciones de tipo, validación, etc.).
Toda la conversión de datos, validación, documentación, etc. seguirá funcionando con normalidad.
De esa manera, podemos declarar solo las diferencias entre los modelos (con contraseña de texto sin formato, con hash_password y sin contraseña):
```
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password: str

def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db

@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved
```

## `Union` o `anyOf`
Puede declarar que una respuesta sea la unión de dos tipos, es decir, que la respuesta sea cualquiera de los dos.
Se definirá en OpenAPI con anyOf.
Para hacer eso, use la escritura de sugerencias de tipo estándar de Python. Unión:

### Nota
Al definir una Unión, incluya primero el tipo más específico, seguido del tipo menos específico. En el siguiente ejemplo, el PlaneItem más específico viene antes de CarItem en Union[PlaneItem, CarItem].

```
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BaseItem(BaseModel):
    description: str
    type: str

class CarItem(BaseItem):
    type = "car"

class PlaneItem(BaseItem):
    type = "plane"
    size: int

items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items[item_id]
```

## Resumen
Use múltiples modelos de Pydantic y herede libremente para cada caso.
No necesita tener un solo modelo de datos por entidad si esa entidad debe poder tener diferentes "estados". Como en el caso del usuario "entidad" con un estado que incluye contraseña, contraseña_hash y sin contraseña.

# Response Status Code
De la misma manera que puede especificar un modelo de respuesta, también puede declarar el código de estado HTTP utilizado para la respuesta con el parámetro status_code  en cualquiera de las operaciones de ruta:

- @aplicación.get()
- @aplicación.post()
- @aplicación.put()
- @aplicación.delete()
- etc.

```
from fastapi import FastAPI

app = FastAPI()


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}
```

Tenga en cuenta que status_code es un parámetro del método "decorador" (obtener, publicar, etc.). No de su función de operación de ruta, como todos los parámetros y el cuerpo.

El parámetro status_code recibe un número con el código de estado HTTP
status_code alternativamente también puede recibir un IntEnum, como http.HTTPStatus de Python.

Algunos códigos de respuesta (consulte la siguiente sección) indican que la respuesta no tiene cuerpo.
FastAPI lo sabe y producirá documentos de OpenAPI que indiquen que no hay un cuerpo de respuesta.

## Acerca de los códigos de estado HTTP
En HTTP, envía un código de estado numérico de 3 dígitos como parte de la respuesta.
Estos códigos de estado tienen asociado un nombre para reconocerlos, pero lo importante es el número.
En breve:

- 100 y más son para "Información". Rara vez los usas directamente. Las respuestas con estos códigos de estado no pueden tener cuerpo.
- 200 y más son para respuestas "Exitosas". Estos son los que más usarías.
- - 200 es el código de estado predeterminado, lo que significa que todo estaba "OK".
- - Otro ejemplo sería 201, "Creado". Se usa comúnmente después de crear un nuevo registro en la base de datos.
- - Un caso especial es 204, "Sin contenido". Esta respuesta se utiliza cuando no hay contenido que devolver al cliente, por lo que la respuesta no debe tener cuerpo.
- 300 y superiores son para "Redireccionamiento". Las respuestas con estos códigos de estado pueden o no tener cuerpo, excepto la 304, "No modificada", que no debe tenerlo.
- 400 y superiores son para respuestas de "Error de cliente". Estos son el segundo tipo que probablemente usaría más.
- - Un ejemplo es 404, para una respuesta "No encontrado".
- - Para errores genéricos del cliente, puede usar 400.
- 500 y superiores son para errores del servidor. Casi nunca los usas directamente. Cuando algo sale mal en alguna parte del código de su aplicación o servidor, devolverá automáticamente uno de estos códigos de estado.

## Atajo para recordar los nombres
Veamos de nuevo el ejemplo anterior:
```
from fastapi import FastAPI

app = FastAPI()

@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}
```

201 es el código de estado para "Creado".
Pero no tienes que memorizar lo que significa cada uno de estos códigos.
Puede utilizar las variables de conveniencia de fastapi.status.
```
from fastapi import FastAPI, status

app = FastAPI()

@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}
```

Son solo una conveniencia, tienen el mismo número, pero de esa manera puede usar el autocompletado del editor para encontrarlos.

# Form Data
Cuando necesite recibir campos de formulario en lugar de JSON, puede usar Form.
Para usar formularios, primero instale python-multipart.
Eje. pip install python-multipart.

## Importar Form
Import Form from fastapi:
```
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
```

## Define Form parameters
Cree parámetros de formulario de la misma manera que lo haría para el cuerpo o la consulta:
```
async def login(username: str = Form(), password: str = Form()):
```

Por ejemplo, en una de las formas en que se puede usar la especificación OAuth2 (llamada "flujo de contraseña"), se requiere enviar un nombre de usuario y una contraseña como campos de formulario.
La especificación requiere que los campos se nombren exactamente como nombre de usuario y contraseña, y que se envíen como campos de formulario, no como JSON.
Con Formulario puede declarar los mismos metadatos y validación que con Cuerpo (y Consulta, Ruta, Cookie).

Para declarar cuerpos de formulario, debe usar Form explícitamente, porque sin él, los parámetros se interpretarían como parámetros de consulta o parámetros de cuerpo (JSON).

## Acerca de "Form Fields"
La forma en que los formularios HTML (<formulario></formulario>) envían los datos al servidor normalmente usa una codificación "especial" para esos datos, es diferente de JSON.
FastAPI se asegurará de leer esos datos desde el lugar correcto en lugar de JSON.

Los datos de los formularios normalmente se codifican utilizando el "tipo de medio" application/x-www-form-urlencoded.
Pero cuando el formulario incluye archivos, se codifica como multipart/form-data. En el próximo capítulo leerá sobre el manejo de archivos.
Si desea leer más sobre estas codificaciones y campos de formulario, diríjase a los documentos web de MDN para POST.

# Manejando Errores
Hay muchas situaciones en las que necesita notificar un error a un cliente que está utilizando su API.
Este cliente podría ser un navegador con una interfaz, un código de otra persona, un dispositivo IoT, etc.
Podría necesitar decirle al cliente que:
- El cliente no tiene suficientes privilegios para esa operación.
- El cliente no tiene acceso a ese recurso.
- El elemento al que el cliente intentaba acceder no existe.
- etc.

En estos casos, normalmente devolvería un código de estado HTTP en el rango de 400 (de 400 a 499).
Esto es similar a los 200 códigos de estado HTTP (del 200 al 299). Esos códigos de estado "200" significan que de alguna manera hubo un "éxito" en la solicitud.
Los códigos de estado en el rango 400 significan que hubo un error del cliente.
¿Recuerdas todos esos errores (y chistes) de "404 no encontrado"?

## Use HTTPException
Para devolver respuestas HTTP con errores al cliente, utiliza HTTPException.

### Importar HTTPException
```
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
```

## Genera una HTTPException en tu código
HTTPException es una excepción normal de Python con datos adicionales relevantes para las API.
Debido a que es una excepción de Python, no lo devuelve, lo genera.
Esto también significa que si está dentro de una función de utilidad a la que está llamando dentro de su función de operación de ruta, y genera la HTTPException desde dentro de esa función de utilidad, no ejecutará el resto del código en la función de operación de ruta, terminará esa solicitud de inmediato y enviará el error HTTP de HTTPException al cliente.
El beneficio de generar una excepción sobre la devolución de un valor será más evidente en la sección sobre dependencias y seguridad.
En este ejemplo, cuando el cliente solicita un artículo con una ID que no existe, genera una excepción con un código de estado de 404:
```
raise HTTPException(status_code=404, detail="Item not found")
```

## La respuesta resultante
Si el cliente solicita http://example.com/items/foo (un item_id "foo"), ese cliente recibirá un código de estado HTTP de 200 y una respuesta JSON de:
```
{
  "item": "The Foo Wrestlers"
}
```

Pero si el cliente solicita http://example.com/items/bar (una "barra" item_id inexistente), ese cliente recibirá un código de estado HTTP de 404 (el error "no encontrado") y una respuesta JSON de:
```
{
  "detail": "Item not found"
}
```

# Dependencies - Primeros pasos
FastAPI tiene un sistema de inyección de dependencia muy poderoso pero intuitivo.
Está diseñado para ser muy simple de usar y para que sea muy fácil para cualquier desarrollador integrar otros componentes con FastAPI.

## ¿Qué es la "inyección de dependencia"?
"Inyección de dependencia" significa, en programación, que hay una manera para que su código (en este caso, sus funciones de operación de ruta) declare las cosas que requiere para funcionar y usar: "dependencias".

Y luego, ese sistema (en este caso, FastAPI) se encargará de hacer lo que sea necesario para proporcionarle a su código las dependencias necesarias ("inyectar" las dependencias).

Esto es muy útil cuando necesitas:

- Tener lógica compartida (la misma lógica de código una y otra vez).
- Compartir conexiones de bases de datos.
- Hacer cumplir los requisitos de seguridad, autenticación, roles, etc.
- Y muchas otras cosas...

Todo esto, mientras minimiza la repetición de código.

## Primeros pasos
Veamos un ejemplo muy sencillo. Será tan sencillo que no es muy útil, por ahora.
Pero de esta manera podemos centrarnos en cómo funciona el sistema de inyección de dependencia.

## Crear una dependencia, o "dependable"
Primero centrémonos en la dependencia.
Es solo una función que puede tomar todos los mismos parámetros que una función de operación de ruta puede tomar:
```
async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}
```

Eso es todo.

### 2 lineas.
Y tiene la misma forma y estructura que tienen todas sus funciones de operación de ruta.
Puede considerarlo como una función de operación de ruta sin el "decorador" (sin @app.get("/some-path")).
Y puede devolver lo que quieras.
En este caso, esta dependencia espera:
- Un parámetro de consulta opcional q que es una cadena.
- Un salto de parámetro de consulta opcional que es un int y, de forma predeterminada, es 0.
- Un límite de parámetro de consulta opcional que es un int y, de forma predeterminada, es 100.

Y luego simplemente devuelve un dictado que contiene esos valores.

## Importar `Depends`
```
from fastapi import Depends, FastAPI
```

## Declarar la dependencia, en el "dependiente"
```
async def read_items(commons: dict = Depends(common_parameters)):
```

Aunque usa Depends en los parámetros de su función de la misma manera que usa Body, Query, etc., Depends funciona de manera un poco diferente.
Solo le das Depende de un solo parámetro.
Este parámetro debe ser algo así como una función.
Y esa función toma parámetros de la misma manera que lo hacen las funciones de operación de ruta.

Cada vez que llega una nueva solicitud, FastAPI se encargará de:
Llamar a su función de dependencia ("dependable") con los parámetros correctos.
Obtenga el resultado de su función.
Asigne ese resultado al parámetro en su función de operación de ruta.

De esta manera, escribe código compartido una vez y FastAPI se encarga de llamarlo para sus operaciones de ruta.

## Uso sencillo
Si lo observa, las funciones de operación de ruta se declaran para usarse siempre que una ruta y una operación coincidan, y luego FastAPI se encarga de llamar a la función con los parámetros correctos, extrayendo los datos de la solicitud.
En realidad, todos (o la mayoría) de los marcos web funcionan de la misma manera.
Nunca llamas a esas funciones directamente. Son llamados por su marco (en este caso, FastAPI).
Con el sistema de Inyección de dependencia, también puede decirle a FastAPI que su función de operación de ruta también "depende" de algo más que debe ejecutarse antes de su función de operación de ruta, y FastAPI se encargará de ejecutarla e "inyectar" los resultados.
Otros términos comunes para esta misma idea de "inyección de dependencia" son:

- resources
- providers
- services
- injectables
- components

# Clases como Dependencies
Antes de profundizar en el sistema de inyección de dependencia, actualicemos el ejemplo anterior.

## Un `dict` del ejemplo anterior.
En el ejemplo anterior, devolvíamos un dictado de nuestra dependencia ("dependable"):
```
async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}
```

Pero luego obtenemos un dict en los parámetros comunes de la función de operación de ruta.
Y sabemos que los editores no pueden proporcionar mucho soporte (como finalización) para dictados, porque no pueden conocer sus claves y tipos de valores.
Podemos hacerlo mejor...

## Qué hace una dependencia
Hasta ahora has visto dependencias declaradas como funciones.
Pero esa no es la única forma de declarar dependencias (aunque probablemente sea la más común).
El factor clave es que una dependencia debe ser "invocable".
Un "invocable" en Python es cualquier cosa que Python pueda "llamar" como una función.
Entonces, si tiene un objeto algo (que podría no ser una función) y puede "llamarlo" (ejecutarlo) como:
```
something()
```

o
```
something(some_argument, some_keyword_argument="foo")
```

entonces es un "invocable".

## Clases como dependencias
Puede notar que para crear una instancia de una clase de Python, usa la misma sintaxis.
Por ejemplo:
```
class Cat:
    def __init__(self, name: str):
        self.name = name


fluffy = Cat(name="Mr Fluffy")
```

En este caso, fluffy es una instancia de la clase Cat.
Y para crear fluffy, estás "llamando" a Cat.
Entonces, una clase de Python también es invocable.
Luego, en FastAPI, podría usar una clase de Python como dependencia.
Lo que FastAPI realmente verifica es que es un "invocable" (función, clase o cualquier otra cosa) y los parámetros definidos.
Si pasa un "invocable" como una dependencia en FastAPI, analizará los parámetros para ese "invocable" y los procesará de la misma manera que los parámetros para una función de operación de ruta. Incluidas las subdependencias.
Eso también se aplica a los invocables sin ningún parámetro. Lo mismo que sería para las funciones de operación de ruta sin parámetros.
Luego, podemos cambiar la dependencia "dependable" common_parameters de arriba a la clase CommonQueryParams:
```
class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit
```

Preste atención al método __init__ utilizado para crear la instancia de la clase:
```
from typing import Union
from fastapi import Depends, FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response
```

...tiene los mismos parámetros que nuestros common_parameters anteriores:
```
from typing import Union
from fastapi import Depends, FastAPI

app = FastAPI()

async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons

@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons
```

Esos parámetros son los que usará FastAPI para "resolver" la dependencia.
En ambos casos, tendrá:

- Un parámetro de consulta q opcional que es una cadena.
- Un parámetro de consulta de omisión que es un int, con un valor predeterminado de 0.
- Un parámetro de consulta de límite que es un int, con un valor predeterminado de 100.
En ambos casos los datos serán convertidos, validados, documentados en el esquema OpenAPI, etc.

## Usalo
Ahora puede declarar su dependencia usando esta clase.
```
from typing import Union
from fastapi import Depends, FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response
```

FastAPI llama a la clase CommonQueryParams. Esto crea una "instancia" de esa clase y la instancia se pasará como parámetro común a su función.

## Type annotation vs Depends
Observe cómo escribimos CommonQueryParams dos veces en el código anterior:
```
commons: CommonQueryParams = Depends(CommonQueryParams)
```

Los últimos CommonQueryParams, en:
```
... = Depends(CommonQueryParams)
```

... es lo que FastAPI realmente usará para saber cuál es la dependencia.
De ahí es que FastAPI extraerá los parámetros declarados y eso es lo que realmente llamará FastAPI.

En este caso, el primer CommonQueryParams, en:
```
commons: CommonQueryParams = Depends(CommonQueryParams)
```

...no tiene ningún significado especial para FastAPI. FastAPI no lo usará para conversión de datos, validación, etc. (ya que está usando = Depends(CommonQueryParams) para eso).

De hecho, podrías escribir simplemente:
```
commons = Depends(CommonQueryParams)
```

## Shortcut
FastAPI proporciona un atajo para estos casos, en los que la dependencia es específicamente una clase a la que FastAPI "llamará" para crear una instancia de la propia clase.

Para esos casos específicos, puede hacer lo siguiente:

En lugar de escribir:
```
commons: CommonQueryParams = Depends(CommonQueryParams)
```

...usted escribe:
```
commons: CommonQueryParams = Depends()
```

Declaras la dependencia como el tipo del parámetro, y usas Depends() como su valor "predeterminado" (que está después del =) para el parámetro de esa función, sin ningún parámetro en Depends(), en lugar de tener que escribir la clase completa de nuevo dentro de Depends(CommonQueryParams).
El mismo ejemplo se vería así:
```
async def read_items(commons: CommonQueryParams = Depends()):
```


...y FastAPI sabrá qué hacer.

# Sub-dependencias
Puede crear dependencias que tengan subdependencias.
Pueden ser tan profundos como necesites que sean.
FastAPI se encargará de solucionarlos.

## Primera dependencia "dependable"
Podría crear una primera dependencia ("dependable") como:
```
def query_extractor(q: Union[str, None] = None):
    return q
```

Declara un parámetro de consulta opcional q como str, y luego simplemente lo devuelve.
Esto es bastante simple (no muy útil), pero nos ayudará a centrarnos en cómo funcionan las subdependencias.

## Segunda dependencia, "dependable" y "dependant"
Luego puede crear otra función de dependencia (una "dependable") que al mismo tiempo declara una dependencia propia (por lo que también es un "dependiente"):
```
def query_or_cookie_extractor(
    q: str = Depends(query_extractor),
    last_query: Union[str, None] = Cookie(default=None),
):
    if not q:
        return last_query
    return q
```

Centrémonos en los parámetros declarados:

- Aunque esta función es una dependencia ("dependable") en sí misma, también declara otra dependencia (que "depende" de otra cosa).
- - Depende del query_extractor, y asigna el valor devuelto por este al parámetro q.
- También declara una cookie last_query opcional, como str.
- - Si el usuario no proporcionó ninguna consulta q, usamos la última consulta utilizada, que guardamos antes en una cookie.

## Usa la dependencia
Entonces podemos usar la dependencia con:
```
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
```

## Usar la misma dependencia varias veces
Si una de sus dependencias se declara varias veces para la misma operación de ruta, por ejemplo, varias dependencias tienen una subdependencia común, FastAPI sabrá llamar a esa subdependencia solo una vez por solicitud.
Y guardará el valor devuelto en un "caché" y lo pasará a todos los "dependientes" que lo necesiten en esa solicitud específica, en lugar de llamar a la dependencia varias veces para la misma solicitud.
En un escenario avanzado en el que sabe que necesita llamar a la dependencia en cada paso (posiblemente varias veces) en la misma solicitud en lugar de usar el valor "almacenado en caché", puede establecer el parámetro use_cache=False al usar Depends:
```
async def needy_dependency(fresh_value: str = Depends(get_value, use_cache=False)):
    return {"fresh_value": fresh_value}
```

## Resumen
Aparte de todas las palabras elegantes que se usan aquí, el sistema de inyección de dependencia es bastante simple.
Solo funciones que tienen el mismo aspecto que las funciones de operación de ruta.
Pero aún así, es muy poderoso y le permite declarar "gráficos" (árboles) de dependencia arbitrariamente anidados.

# Dependencias en path operation decorators
En algunos casos, realmente no necesita el valor de retorno de una dependencia dentro de su función de operación de ruta.
O la dependencia no devuelve un valor.
Pero aún necesita que se ejecute / resuelva.
Para esos casos, en lugar de declarar un parámetro de función de operación de ruta con Depends, puede agregar una lista de dependencias al decorador de operación de ruta.

## Agregar dependencias a los path operation decorator
El decorador de la operación de ruta recibe un argumento opcional de dependencias.
Debería ser una lista de Depends():
```
from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()

async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key

@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
```

Estas dependencias se ejecutarán/resolverán de la misma manera que las dependencias normales. Pero su valor (si devuelven alguno) no se pasará a su función de operación de ruta.

## Errores de dependencias y valores devueltos
Puede usar las mismas funciones de dependencia que usa normalmente.

# Dependencias Globales
Para algunos tipos de aplicaciones, es posible que desee agregar dependencias a toda la aplicación.
De forma similar a como puede agregar dependencias a los decoradores de operaciones de ruta, puede agregarlos a la aplicación FastAPI.
En ese caso, se aplicarán a todas las operaciones de ruta en la aplicación:
```
from fastapi import Depends, FastAPI, Header, HTTPException

async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key

app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])

@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]

@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
```

Y todas las ideas de la sección sobre cómo agregar dependencias a los decoradores de operaciones de ruta aún se aplican, pero en este caso, a todas las operaciones de ruta en la aplicación.

# Introducción a la seguridad
Hay muchas formas de manejar la seguridad, la autenticación y la autorización.
Y normalmente es un tema complejo y "difícil".
En muchos marcos y sistemas, solo manejar la seguridad y la autenticación requiere una gran cantidad de esfuerzo y código (en muchos casos, puede ser el 50% o más de todo el código escrito).
FastAPI proporciona varias herramientas para ayudarlo a lidiar con la seguridad de manera fácil, rápida y estándar, sin tener que estudiar y aprender todas las especificaciones de seguridad.
Pero primero, revisemos algunos pequeños conceptos.

## OAuth2
OAuth2 es una especificación que define varias formas de manejar la autenticación y la autorización.
Es una especificación bastante extensa y cubre varios casos de uso complejos.
Incluye formas de autenticación mediante un "tercero".
Eso es lo que usan debajo todos los sistemas con "iniciar sesión con Facebook, Google, Twitter, GitHub".

## OAuth 1
Existía un OAuth 1, que es muy diferente al OAuth2, y más complejo, ya que incluía directamente especificaciones sobre cómo encriptar la comunicación.
No es muy popular o utilizado hoy en día.
OAuth2 no especifica cómo cifrar la comunicación, espera que su aplicación se sirva con HTTPS.

## OpenID Connect
OpenID Connect es otra especificación, basada en OAuth2.
Simplemente extiende OAuth2 especificando algunas cosas que son relativamente ambiguas en OAuth2, para intentar hacerlo más interoperable.
Por ejemplo, el inicio de sesión de Google usa OpenID Connect (que debajo usa OAuth2).
Pero el inicio de sesión de Facebook no es compatible con OpenID Connect. Tiene su propio sabor de OAuth2.

## OpenID (not "OpenID Connect")
También había una especificación "OpenID". Eso intentó resolver lo mismo que OpenID Connect, pero no se basó en OAuth2.
Entonces, era un sistema adicional completo.
No es muy popular o utilizado hoy en día.

## OpenAPI
OpenAPI (anteriormente conocido como Swagger) es la especificación abierta para crear API (ahora parte de Linux Foundation).
FastAPI se basa en OpenAPI.
Eso es lo que hace posible tener múltiples interfaces automáticas de documentación interactiva, generación de código, etc.
OpenAPI tiene una forma de definir múltiples "esquemas" de seguridad.
Al usarlos, puede aprovechar todas estas herramientas basadas en estándares, incluidos estos sistemas de documentación interactivos.
OpenAPI define los siguientes esquemas de seguridad:
- apiKey: una clave específica de la aplicación que puede provenir de:
- - Un parámetro de consulta- .
- - Un encabezado.
- - Una cockie.
- http: sistemas de autenticación HTTP estándar, que incluyen:
- - bearer: una Autorización de encabezado con un valor de bearer más un token. Esto se hereda de OAuth2.
- - Autenticación básica HTTP.
- - HTTP Digest, etc.
- oauth2: todas las formas OAuth2 de manejar la seguridad (llamadas "flujos").
- - Varios de estos flujos son apropiados para construir un proveedor de autenticación OAuth 2.0 (como Google, Facebook, Twitter, GitHub, etc.):
- - - implícito
- - - Credenciales del cliente
- - - Código de Autorización
-  hay un "flujo" específico que se puede usar perfectamente para manejar la autenticación en la misma aplicación directamente:
- - contraseña: algunos capítulos siguientes cubrirán ejemplos de esto.
- openIdConnect: tiene una forma de definir cómo descubrir los datos de autenticación OAuth2 automáticamente.
- - Este descubrimiento automático es lo que se define en la especificación de OpenID Connect.

## FastAPI utilities
FastAPI proporciona varias herramientas para cada uno de estos esquemas de seguridad en el módulo fastapi.security que simplifican el uso de estos mecanismos de seguridad.
En los próximos capítulos, verá cómo agregar seguridad a su API utilizando las herramientas proporcionadas por FastAPI.
Y también verás cómo se integra automáticamente en el sistema de documentación interactivo.

# Security - Primeros Pasos
Imaginemos que tiene su API de back-end en algún dominio.
Y tienes un frontend en otro dominio o en una ruta diferente del mismo dominio (o en una aplicación móvil).
Y desea tener una forma para que el frontend se autentique con el backend, usando un nombre de usuario y una contraseña.
Podemos usar OAuth2 para construir eso con FastAPI.
Pero ahorrémosle el tiempo de leer la especificación larga completa solo para encontrar los pequeños fragmentos de información que necesita.
Usemos las herramientas provistas por FastAPI para manejar la seguridad.

## Como luce
Primero usemos el código y veamos cómo funciona, y luego volveremos para entender qué está pasando.

## Crear main.py
Copie el ejemplo en un archivo main.py:
```
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

## Ejecutalo
Primero instale python-multipart.
P.ej. pip install python-multipart.
Esto se debe a que OAuth2 usa "datos de formulario" para enviar el nombre de usuario y la contraseña.
```
uvicorn main:app --reload
```

Ya tienes un nuevo y brillante botón "Autorizar".
Y su operación de ruta tiene un pequeño candado en la esquina superior derecha en el que puede hacer clic.

## El flujo de password
Ahora retrocedamos un poco y entendamos qué es todo eso.
La contraseña "flow" es una de las formas ("flows") definidas en OAuth2, para manejar la seguridad y la autenticación.
OAuth2 fue diseñado para que el backend o API pudiera ser independiente del servidor que autentica al usuario.
Pero en este caso, la misma aplicación FastAPI manejará la API y la autenticación.
Entonces, repasemos desde ese punto de vista simplificado:
- El usuario escribe el nombre de usuario y la contraseña en la interfaz y presiona Enter.
- La interfaz (que se ejecuta en el navegador del usuario) envía ese nombre de usuario y contraseña a una URL específica en nuestra API (declarada con tokenUrl="token").
- La API verifica ese nombre de usuario y contraseña, y responde con un "token" (todavía no hemos implementado nada de esto).
- - Un "token" es solo una cadena con algún contenido que podemos usar más adelante para verificar a este usuario.
- - Normalmente, un token está configurado para caducar después de un tiempo.
- - - Por lo tanto, el usuario tendrá que iniciar sesión nuevamente en algún momento posterior.
- - - Y si el token es robado, el riesgo es menor. No es como una clave permanente que funcionará para siempre (en la mayoría de los casos).
- La interfaz almacena ese token temporalmente en algún lugar.
- El usuario hace clic en la interfaz para ir a otra sección de la aplicación web de la interfaz.
- La interfaz necesita obtener más datos de la API.
- - Pero necesita autenticación para ese punto final específico.
- - Entonces, para autenticarse con nuestra API, envía una Autorización de encabezado con un valor de Bearer más el token.
- - Si el token contiene foobar, el contenido del encabezado de autorización sería: Bearer foobar.

## FastAPI OAuth2PasswordBearer
FastAPI proporciona varias herramientas, en diferentes niveles de abstracción, para implementar estas funciones de seguridad.
En este ejemplo vamos a usar OAuth2, con el flujo de Contraseña, usando un token de bearer. Hacemos eso usando la clase OAuth2PasswordBearer.

Un token "bearer" no es la única opción.
Pero es el mejor para nuestro caso de uso.
Y podría ser lo mejor para la mayoría de los casos de uso, a menos que sea un experto en OAuth2 y sepa exactamente por qué hay otra opción que se adapta mejor a sus necesidades.
En ese caso, FastAPI también le proporciona las herramientas para construirlo.

Cuando creamos una instancia de la clase OAuth2PasswordBearer, pasamos el parámetro tokenUrl. Este parámetro contiene la URL que el cliente (la interfaz que se ejecuta en el navegador del usuario) utilizará para enviar el nombre de usuario y la contraseña para obtener un token.
```
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```

Aquí tokenUrl="token" se refiere a un token de URL relativo que aún no hemos creado. Como es una URL relativa, es equivalente a ./token.
Debido a que estamos usando una URL relativa, si su API estuviera ubicada en https://example.com/, entonces se referiría a https://example.com/token. Pero si su API estuviera ubicada en https://example.com/api/v1/, entonces se referiría a https://example.com/api/v1/token.
El uso de una URL relativa es importante para asegurarse de que su aplicación siga funcionando incluso en un caso de uso avanzado como Behind a Proxy.

Este parámetro no crea esa operación de punto final/ruta, pero declara que la URL/token será la que el cliente debe usar para obtener el token. Esa información se usa en OpenAPI y luego en los sistemas de documentación de API interactivos.
Pronto crearemos también la operación de ruta real.

La variable oauth2_scheme es una instancia de OAuth2PasswordBearer, pero también es "invocable".
Podría llamarse como:
```
oauth2_scheme(some, parameters)
```

Por lo tanto, se puede usar con Depends.

## Uselo
Ahora puede pasar ese oauth2_scheme en una dependencia con Depends.
```
async def read_items(token: str = Depends(oauth2_scheme)):
```

Esta dependencia proporcionará un str que se asigna al token de parámetro de la función de operación de ruta.
FastAPI sabrá que puede usar esta dependencia para definir un "esquema de seguridad" en el esquema de OpenAPI (y los documentos de API automáticos).

FastAPI sabrá que puede usar la clase OAuth2PasswordBearer (declarada en una dependencia) para definir el esquema de seguridad en OpenAPI porque hereda de fastapi.security.oauth2.OAuth2, que a su vez hereda de fastapi.security.base.SecurityBase.
Todas las utilidades de seguridad que se integran con OpenAPI (y los documentos automáticos de API) heredan de SecurityBase, así es como FastAPI puede saber cómo integrarlas en OpenAPI.

## Que hace
Irá y buscará en la solicitud ese encabezado de Autorización, verificará si el valor es bearer más algún token, y devolverá el token como una cadena.
Si no ve un encabezado de autorización o el valor no tiene un token de bearer, responderá directamente con un error de código de estado 401 (NO AUTORIZADO).
Ni siquiera tiene que verificar si el token existe para devolver un error. Puede estar seguro de que si se ejecuta su función, tendrá una cadena en ese token.
Ya puedes probarlo en los documentos interactivos.
Todavía no estamos verificando la validez del token, pero eso ya es un comienzo.

## Resumen
Entonces, en solo 3 o 4 líneas adicionales, ya tiene alguna forma primitiva de seguridad.

# Obtener usuario actual
En el capítulo anterior, el sistema de seguridad (que se basa en el sistema de inyección de dependencia) le daba a la función de operación de ruta un token como str:
```
async def read_items(token: str = Depends(oauth2_scheme)):
```

Pero eso todavía no es tan útil.
Hagamos que nos dé el usuario actual.

## Crear un modelo de usuario
Primero, creemos un modelo de usuario de Pydantic.
De la misma manera que usamos Pydantic para declarar cuerpos, podemos usarlo en cualquier otro lugar:
```
from typing import Union
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
```

## Crear una dependencia get_current_user
Vamos a crear una dependencia get_current_user.
¿Recuerdas que las dependencias pueden tener subdependencias?
get_current_user tendrá una dependencia con el mismo oauth2_scheme que creamos antes.
Al igual que hacíamos antes en la operación de ruta directamente, nuestra nueva dependencia get_current_user recibirá un token como str de la subdependencia oauth2_scheme:
```
from typing import Union
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
```

## Obtener el usuario
get_current_user utilizará una función de utilidad (falsa) que creamos, que toma un token como str y devuelve nuestro modelo Pydantic User:
```
def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user
```

## Inyectar al usuario actual
Así que ahora podemos usar el mismo Depende con nuestro get_current_user en la operación de ruta:
```
async def read_users_me(current_user: User = Depends(get_current_user)):
```

Tenga en cuenta que declaramos el tipo de current_user como el usuario del modelo Pydantic.
Esto nos ayudará dentro de la función con todas las verificaciones de finalización y tipo.

## Otros modelos
Ahora puede obtener al usuario actual directamente en las funciones de operación de ruta y manejar los mecanismos de seguridad en el nivel de Inyección de Dependencia, usando Depends.
Y puede usar cualquier modelo o datos para los requisitos de seguridad (en este caso, un usuario modelo de Pydantic).
Pero no está restringido a usar algún modelo, clase o tipo de datos específico.
¿Quieres tener una identificación y un correo electrónico y no tener ningún nombre de usuario en tu modelo? Por supuesto. Puedes usar estas mismas herramientas.
¿Quieres tener sólo una str? ¿O simplemente un dictado? ¿O una instancia de modelo de clase de base de datos directamente? Todo funciona de la misma manera.
¿Realmente no tiene usuarios que inicien sesión en su aplicación sino robots, bots u otros sistemas que solo tienen un token de acceso? De nuevo, todo funciona igual.
Simplemente use cualquier tipo de modelo, cualquier tipo de clase, cualquier tipo de base de datos que necesite para su aplicación. FastAPI lo tiene cubierto con el sistema de inyección de dependencia.

## Tamaño del código
Este ejemplo puede parecer detallado. Tenga en cuenta que estamos mezclando seguridad, modelos de datos, funciones de utilidad y operaciones de ruta en el mismo archivo.
Pero aquí está el punto clave.
Las cosas de inyección de seguridad y dependencia se escriben una vez.
Y puedes hacerlo tan complejo como quieras. Y aún así, tenerlo escrito una sola vez, en un solo lugar. Con toda la flexibilidad.
Pero puede tener miles de puntos finales (operaciones de ruta) utilizando el mismo sistema de seguridad.
Y todos ellos (o cualquier parte de ellos que desee) pueden aprovechar la reutilización de estas dependencias o cualquier otra dependencia que cree.
Y todas estas miles de operaciones de ruta pueden ser tan pequeñas como 3 líneas:
```
@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
```

## Resumen
Ahora puede obtener el usuario actual directamente en su función de operación de ruta.
Ya estamos a mitad de camino.
Solo necesitamos agregar una operación de ruta para que el usuario/cliente envíe el nombre de usuario y la contraseña.
Eso viene después.

# OAuth2 simple con contraseña y portador
Ahora, construyamos a partir del capítulo anterior y agreguemos las partes que faltan para tener un flujo de seguridad completo.

## Obtenga el nombre de usuario y la contraseña
Vamos a utilizar las utilidades de seguridad FastAPI para obtener el nombre de usuario y la contraseña.
OAuth2 especifica que al usar el "flujo de contraseña" (que estamos usando) el cliente/usuario debe enviar un campo de nombre de usuario y contraseña como datos del formulario.
Y la especificación dice que los campos deben nombrarse así. Entonces, el nombre de usuario o el correo electrónico no funcionarían.
Pero no te preocupes, puedes mostrarlo como quieras a tus usuarios finales en la interfaz.
Y sus modelos de base de datos pueden usar cualquier otro nombre que desee.
Pero para la operación de ruta de inicio de sesión, necesitamos usar estos nombres para que sean compatibles con la especificación (y poder, por ejemplo, usar el sistema de documentación API integrado).
La especificación también establece que el nombre de usuario y la contraseña deben enviarse como datos de formulario (por lo tanto, no hay JSON aquí).

## `scope`
La especificación también dice que el cliente puede enviar otro campo de formulario "scope".
El nombre del campo de formulario es scope (en singular), pero en realidad es una cadena larga con "scope" separados por espacios.
Cada "scope" es solo una cadena (sin espacios).
Normalmente se utilizan para declarar permisos de seguridad específicos, por ejemplo:
- users:read o users:write son ejemplos comunes.
- instagram_basic es utilizado por Facebook / Instagram.
- Google utiliza https://www.googleapis.com/auth/drive.

En OAuth2, un "scope" es solo una cadena que declara que se requiere un permiso específico.
No importa si tiene otros caracteres como: o si es una URL.
Esos detalles son específicos de la implementación.
Para OAuth2 son solo cadenas.

## Código para obtener el usuario y la contraseña
Ahora usemos las utilidades provistas por FastAPI para manejar esto.

### OAuth2PasswordRequestForm
Primero, importe OAuth2PasswordRequestForm y utilícelo como una dependencia con Depends en la operación de ruta para /token:
```
from typing import Union
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
```

OAuth2PasswordRequestForm es una dependencia de clase que declara el cuerpo de un formulario con:

- El nombre de usuario.
- La contraseña.
- Un campo de alcance opcional como una gran cadena, compuesta de cadenas separadas por espacios.
- Un tipo de subvención opcional.
- Un client_id opcional (no lo necesitamos para nuestro ejemplo).
- Un client_secret opcional (no lo necesitamos para nuestro ejemplo).

La especificación OAuth2 en realidad requiere un campo grant_type con un valor fijo de contraseña, pero OAuth2PasswordRequestForm no lo impone.
Si necesita aplicarlo, use OAuth2PasswordRequestFormStrict en lugar de OAuth2PasswordRequestForm.
OAuth2PasswordRequestForm no es una clase especial para FastAPI como lo es OAuth2PasswordBearer.
OAuth2PasswordBearer hace que FastAPI sepa que es un esquema de seguridad. Entonces se agrega de esa manera a OpenAPI.
Pero OAuth2PasswordRequestForm es solo una dependencia de clase que podría haber escrito usted mismo, o podría haber declarado parámetros de formulario directamente.
Pero como es un caso de uso común, FastAPI lo proporciona directamente, solo para hacerlo más fácil.

## Usa los datos del formulario
La instancia de la clase de dependencia OAuth2PasswordRequestForm no tendrá un scope de atributo con la cadena larga separada por espacios, sino que tendrá un atributo de scope con la lista real de cadenas para cada scope enviado.
No estamos usando scopes en este ejemplo, pero la funcionalidad está ahí si la necesita.

Ahora, obtenga los datos del usuario de la base de datos (falsa), utilizando el nombre de usuario del campo de formulario.
Si no existe tal usuario, devolvemos un error que dice "nombre de usuario o contraseña incorrectos".
Para el error, usamos la excepción HTTPException:
```
user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
```

## Verifique la contraseña
En este punto tenemos los datos de usuario de nuestra base de datos, pero no hemos comprobado la contraseña.
Primero pongamos esos datos en el modelo Pydantic UserInDB.
Nunca debe guardar contraseñas de texto sin formato, por lo tanto, usaremos el sistema de hashing de contraseñas (falsas).
Si las contraseñas no coinciden, devolvemos el mismo error.

### Password hashing
"Hashing" significa: convertir algún contenido (una contraseña en este caso) en una secuencia de bytes (solo una cadena) que parece un galimatías.
Cada vez que pasa exactamente el mismo contenido (exactamente la misma contraseña) obtiene exactamente el mismo galimatías.
Pero no puede convertir el galimatías a la contraseña.

#### POR QUÉ UTILIZAR HASH DE CONTRASEÑA
Si le roban su base de datos, el ladrón no tendrá las contraseñas de texto sin formato de sus usuarios, solo los hashes.
Por lo tanto, el ladrón no podrá intentar usar esas mismas contraseñas en otro sistema (ya que muchos usuarios usan la misma contraseña en todas partes, esto sería peligroso).
```
 user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
```

## Acerca de **user_dict
UserInDB(**user_dict) significa:
Pase las claves y los valores de user_dict directamente como argumentos de clave-valor, equivalentes a:
```
UserInDB(
    username = user_dict["username"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
    disabled = user_dict["disabled"],
    hashed_password = user_dict["hashed_password"],
)
```

## Retorna el token
La respuesta del extremo del token debe ser un objeto JSON.
Debe tener un token_type. En nuestro caso, como estamos usando tokens "Bearer", el tipo de token debe ser "bearer".
Y debería tener un access_token, con una cadena que contenga nuestro token de acceso.
Para este ejemplo simple, vamos a ser completamente inseguros y devolveremos el mismo nombre de usuario que el token.

En el próximo capítulo, verá una implementación realmente segura, con hash de contraseña y tokens JWT.
Pero por ahora, concentrémonos en los detalles específicos que necesitamos.

```
return {"access_token": user.username, "token_type": "bearer"}
```

Según la especificación, debe devolver un JSON con access_token y token_type, igual que en este ejemplo.
Esto es algo que debe hacer usted mismo en su código y asegúrese de usar esas claves JSON.
Es casi lo único que debe recordar para hacer correctamente usted mismo, para cumplir con las especificaciones.
Por lo demás, FastAPI lo maneja por usted.

## Actualizar las dependencias
Ahora vamos a actualizar nuestras dependencias.
Queremos obtener el usuario actual solo si este usuario está activo.
Entonces, creamos una dependencia adicional get_current_active_user que a su vez usa get_current_user como dependencia.
Ambas dependencias solo devolverán un error HTTP si el usuario no existe o si está inactivo.
Entonces, en nuestro punto final, solo obtendremos un usuario si el usuario existe, se autenticó correctamente y está activo:
```
async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
```

El encabezado adicional WWW-Authenticate con valor Bearer que devolvemos aquí también es parte de la especificación.
Se supone que cualquier código de estado HTTP (error) 401 "NO AUTORIZADO" también devolverá un encabezado WWW-Authenticate.
En el caso de los tokens bearer  (nuestro caso), el valor de ese encabezado debe ser bearer.
En realidad, puede omitir ese encabezado adicional y aún funcionaría.
Pero se proporciona aquí para cumplir con las especificaciones.
Además, puede haber herramientas que lo esperen y lo usen (ahora o en el futuro) y que puedan ser útiles para usted o sus usuarios, ahora o en el futuro.
Ese es el beneficio de los estándares...

## Resumen
Ahora tienes las herramientas para implementar un completo sistema de seguridad basado en usuario y contraseña para tu API.
Con estas herramientas, puede hacer que el sistema de seguridad sea compatible con cualquier base de datos y con cualquier usuario o modelo de datos.
El único detalle que falta es que todavía no es "seguro".
En el próximo capítulo, verá cómo usar una biblioteca segura de hash de contraseñas y tokens JWT.

# OAuth2 con contraseña (y hashing), bearer con tokens JWT
Ahora que tenemos todo el flujo de seguridad, hagamos que la aplicación sea realmente segura, usando tokens JWT y hash de contraseña seguro.
Este código es algo que realmente puede usar en su aplicación, guardar los hashes de contraseña en su base de datos, etc.
Vamos a empezar desde donde lo dejamos en el capítulo anterior e incrementarlo.

## Sobre JWT
JWT significa "tokens web JSON".
Es un estándar para codificar un objeto JSON en una cadena larga y densa sin espacios. Se parece a esto:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

No está encriptado, por lo que cualquiera podría recuperar la información de los contenidos.
Pero está firmado. Entonces, cuando recibe un token que emitió, puede verificar que realmente lo emitió.
De esa forma, puede crear un token con una caducidad de, digamos, 1 semana. Y luego, cuando el usuario regresa al día siguiente con el token, sabe que el usuario todavía está conectado a su sistema.
Después de una semana, el token caducará y el usuario no estará autorizado y deberá iniciar sesión nuevamente para obtener un nuevo token. Y si el usuario (o un tercero) intentara modificar el token para cambiar la caducidad, podría descubrirlo, porque las firmas no coincidirían.
Si quiere jugar con tokens JWT y ver cómo funcionan, consulte https://jwt.io.

## Instalar python-jose
Necesitamos instalar python-jose para generar y verificar los tokens JWT en Python:
```
pip install "python-jose[cryptography]"
```

Python-jose requiere un backend criptográfico como extra.
Aquí estamos usando el recomendado: pyca/cryptography.

Este tutorial utilizó anteriormente PyJWT.
Pero se actualizó para usar Python-jose en su lugar, ya que proporciona todas las funciones de PyJWT más algunos extras que podría necesitar más adelante al crear integraciones con otras herramientas.

## Hash de contraseña
"Hashing" significa convertir algún contenido (una contraseña en este caso) en una secuencia de bytes (solo una cadena) que parece un galimatías.
Cada vez que pasa exactamente el mismo contenido (exactamente la misma contraseña) obtiene exactamente el mismo galimatías.
Pero no puede convertir el galimatías a la contraseña.

### ¿Por qué usar hash de contraseña?
Si le roban su base de datos, el ladrón no tendrá las contraseñas de texto sin formato de sus usuarios, solo los hashes.
Por lo tanto, el ladrón no podrá intentar usar esa contraseña en otro sistema (ya que muchos usuarios usan la misma contraseña en todas partes, esto sería peligroso).

## Install passlib
PassLib es un excelente paquete de Python para manejar hashes de contraseñas.
Admite muchos algoritmos de hash seguros y utilidades para trabajar con ellos.
El algoritmo recomendado es "Bcrypt".
Entonces, instala PassLib con Bcrypt:
```
pip install "passlib[bcrypt]"
```

Con passlib, incluso puede configurarlo para poder leer contraseñas creadas por Django, un complemento de seguridad Flask o muchos otros.
Entonces, podría, por ejemplo, compartir los mismos datos de una aplicación Django en una base de datos con una aplicación FastAPI. O migre gradualmente una aplicación Django utilizando la misma base de datos.
Y sus usuarios podrán iniciar sesión desde su aplicación Django o desde su aplicación FastAPI, al mismo tiempo.


## Hash y verificar las contraseñas
Importa las herramientas que necesitamos de passlib.
Cree un "contexto" PassLib. Esto es lo que se usará para codificar y verificar contraseñas.

El contexto PassLib también tiene funcionalidad para usar diferentes algoritmos hash, incluidos los antiguos obsoletos solo para permitir verificarlos, etc.
Por ejemplo, podría usarlo para leer y verificar contraseñas generadas por otro sistema (como Django) pero codificar las contraseñas nuevas con un algoritmo diferente como Bcrypt.
Y ser compatible con todos ellos al mismo tiempo.

Cree una función de utilidad para codificar una contraseña proveniente del usuario.
Y otra utilidad para verificar si una contraseña recibida coincide con el hash almacenado.
Y otro para autenticar y devolver un usuario.
```
from datetime import datetime, timedelta
from typing import Union

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

class UserInDB(User):
    hashed_password: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
```

Si revisa la nueva base de datos (falsa) fake_users_db, verá cómo se ve ahora la contraseña cifrada: "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW".

## Manejar tokens JWT
Importar los módulos instalados.
Cree una clave secreta aleatoria que se usará para firmar los tokens JWT.
Para generar una clave secreta aleatoria segura, use el comando:

```
openssl rand -hex 32
```

Y copie la salida a la variable SECRET_KEY (no use la del ejemplo).
Cree un ALGORITMO variable con el algoritmo utilizado para firmar el token JWT y configúrelo en "HS256".
Cree una variable para el vencimiento del token.
Defina un modelo Pydantic que se usará en el extremo del token para la respuesta.
Cree una función de utilidad para generar un nuevo token de acceso.
```
from jose import JWTError, jwt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```

## Update the dependencies
Actualice get_current_user para recibir el mismo token que antes, pero esta vez, utilizando tokens JWT.
Decodifique el token recibido, verifíquelo y devuelva el usuario actual.
Si el token no es válido, devuelva un error HTTP de inmediato.
```
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
```

## Actualizar la /token path operation
Cree un timedelta con el tiempo de vencimiento del token.
Cree un token de acceso JWT real y devuélvalo.

```
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
```

## Detalles técnicos sobre el sub "subject" de JWT
La especificación JWT dice que hay una clave sub, con el subject del token.
Es opcional usarlo, pero ahí es donde colocaría la identificación del usuario, así que lo estamos usando aquí.
JWT puede usarse para otras cosas además de identificar a un usuario y permitirle realizar operaciones directamente en su API.
Por ejemplo, podría identificar un "automóvil" o una "publicación de blog".
Luego, podría agregar permisos sobre esa entidad, como "conducir" (para el automóvil) o "editar" (para el blog).
Y luego, podría darle ese token JWT a un usuario (o bot), y podría usarlo para realizar esas acciones (conducir el automóvil o editar la publicación del blog) sin siquiera necesitar tener una cuenta, solo con el token JWT. su API generada para eso.
Usando estas ideas, JWT se puede usar para escenarios mucho más sofisticados.
En esos casos, varias de esas entidades podrían tener la misma ID, digamos foo (un usuario foo, un automóvil foo y una publicación de blog foo).
Por lo tanto, para evitar colisiones de ID, al crear el token JWT para el usuario, puede prefijar el valor de la subclave, p. con nombre de usuario:. Entonces, en este ejemplo, el valor de sub podría haber sido: nombre de usuario: johndoe.
Lo importante a tener en cuenta es que la clave secundaria debe tener un identificador único en toda la aplicación y debe ser una cadena.

## Resumen
Con lo que has visto hasta ahora, puedes configurar una aplicación FastAPI segura usando estándares como OAuth2 y JWT.
En casi cualquier marco, el manejo de la seguridad se convierte rápidamente en un tema bastante complejo.
Muchos paquetes que lo simplifican mucho tienen que hacer muchos compromisos con el modelo de datos, la base de datos y las funciones disponibles. Y algunos de estos paquetes que simplifican demasiado las cosas en realidad tienen fallas de seguridad debajo.

# Middleware
Puede agregar middleware a las aplicaciones FastAPI.
Un "middleware" es una función que funciona con cada solicitud antes de que sea procesada por cualquier operación de ruta específica. Y también con cada respuesta antes de devolverla.
- Toma cada solicitud que llega a su aplicación.
- Luego puede hacer algo con esa solicitud o ejecutar cualquier código necesario.
- Luego pasa la solicitud para que sea procesada por el resto de la aplicación (mediante alguna operación de ruta).
- Luego toma la respuesta generada por la aplicación (mediante alguna operación de ruta).
- Puede hacer algo con esa respuesta o ejecutar cualquier código necesario.
- Luego devuelve la respuesta.

## Crear un middleware
Para crear un middleware, utiliza el decorador @app.middleware("http") encima de una función.
La función de middleware recibe:

- La solicitud.
- Una función call_next que recibirá la solicitud como parámetro.
- - Esta función pasará la solicitud a la operación de ruta correspondiente.
- - Luego devuelve la respuesta generada por la operación de ruta correspondiente.
- A continuación, puede modificar aún más la respuesta antes de devolverla.
```
import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

## Antes y después de la respuesta.
Puede agregar código para que se ejecute con la solicitud, antes de que lo reciba cualquier operación de ruta.
Y también después de que se genera la respuesta, antes de devolverla.
Por ejemplo, podría agregar un encabezado personalizado X-Process-Time que contenga el tiempo en segundos que tomó procesar la solicitud y generar una respuesta:
```
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

# CORS (Cross-Origin Resource Sharing)
CORS o "Intercambio de recursos de origen cruzado" se refiere a las situaciones en las que una interfaz que se ejecuta en un navegador tiene código JavaScript que se comunica con un backend, y el backend está en un "origen" diferente al de la interfaz.

## Origin
Un origen es la combinación de protocolo (http, https), dominio (myapp.com, localhost, localhost.tiangolo.com) y puerto (80, 443, 8080).
Entonces, todos estos son orígenes diferentes:
- http://localhost
- https://localhost
- http://localhost:8080

Incluso si están todos en localhost, usan diferentes protocolos o puertos, por lo que son "orígenes" diferentes.

## Pasos
Entonces, supongamos que tiene una interfaz ejecutándose en su navegador en http://localhost:8080, y su JavaScript intenta comunicarse con un servidor que se ejecuta en http://localhost (porque no especificamos un puerto, el navegador asumirá el puerto predeterminado 80).
Luego, el navegador enviará una solicitud de OPCIONES HTTP al backend, y si el backend envía los encabezados apropiados que autorizan la comunicación desde este origen diferente (http://localhost:8080), entonces el navegador permitirá que el JavaScript en el frontend envíe su solicitud al backend.
Para lograr esto, el backend debe tener una lista de "orígenes permitidos".
En este caso, tendría que incluir http://localhost:8080 para que la interfaz funcione correctamente.

## Wildcards
También es posible declarar la lista como "*" (un "comodín") para decir que todos están permitidos.
Pero eso solo permitirá cierto tipo de comunicación, excluyendo todo lo que involucre credenciales: Cookies, Encabezados de autorización como los que se usan con los Bearer Tokens, etc.
Entonces, para que todo funcione correctamente, es mejor especificar explícitamente los orígenes permitidos.

## Use CORSMiddleware
Puede configurarlo en su aplicación FastAPI utilizando CORSMiddleware.
- Importar CORSMiddleware.
- Cree una lista de orígenes permitidos (como cadenas).
- Agréguelo como un "middleware" a su aplicación FastAPI.

También puede especificar si su backend permite:
- Credenciales (Cabeceras de Autorización, Cookies, etc).
- Métodos HTTP específicos (POST, PUT) o todos ellos con el comodín "*".
- Cabeceras HTTP específicas o todas ellas con el comodín "*".

```
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}
```

Los parámetros predeterminados utilizados por la implementación de CORSMiddleware son restrictivos de forma predeterminada, por lo que deberá habilitar explícitamente orígenes, métodos o encabezados particulares para que los navegadores puedan usarlos en un contexto de dominio cruzado.
Se admiten los siguientes argumentos:
- allow_origins: una lista de orígenes a los que se debe permitir realizar solicitudes de origen cruzado. P.ej. ['https://ejemplo.org', 'https://www.ejemplo.org']. Puede usar ['*'] para permitir cualquier origen.
- allow_origin_regex: una cadena de expresiones regulares para comparar con los orígenes a los que se debe permitir realizar solicitudes de origen cruzado. p.ej. 'https://.*\.ejemplo\.org'.
- allow_methods: una lista de métodos HTTP que deben permitirse para solicitudes de origen cruzado. El valor predeterminado es ['GET']. Puede usar ['*'] para permitir todos los métodos estándar.
- allow_headers: una lista de encabezados de solicitud HTTP que deben admitirse para solicitudes de origen cruzado. El valor predeterminado es []. Puede usar ['*'] para permitir todos los encabezados. Los encabezados Accept, Accept-Language, Content-Language y Content-Type siempre están permitidos para las solicitudes de CORS.
- allow_credentials: indica que las cookies deben admitirse para solicitudes de origen cruzado. El valor predeterminado es falso. Además, allow_origins no se puede establecer en ['*'] para que se permitan las credenciales, se deben especificar los orígenes.
- expone_headers: indica los encabezados de respuesta que deben estar accesibles para el navegador. El valor predeterminado es [].
- max_age: establece un tiempo máximo en segundos para que los navegadores almacenen en caché las respuestas de CORS. El valor predeterminado es 600.

El middleware responde a dos tipos particulares de solicitud HTTP...

## Solicitudes de verificación previa de CORS
Estas son cualquier solicitud de OPCIONES con encabezados Origin y Access-Control-Request-Method.
En este caso, el middleware interceptará la solicitud entrante y responderá con los encabezados CORS apropiados y una respuesta 200 o 400 con fines informativos.

## Solicitudes simples
Cualquier solicitud con un encabezado de origen. En este caso, el middleware pasará la solicitud de forma normal, pero incluirá los encabezados CORS apropiados en la respuesta.

# SQL (Relational) Databases
FastAPI no requiere que use una base de datos SQL (relacional).
Pero puede usar cualquier base de datos relacional que desee.
Aquí veremos un ejemplo usando SQLAlchemy.
Puede adaptarlo fácilmente a cualquier base de datos compatible con SQLAlchemy, como:
- PostgreSQL
- MySQL
- SQLite
- Oracle
- Microsoft SQL Server, etc.

En este ejemplo, usaremos SQLite, porque usa un solo archivo y Python tiene soporte integrado. Entonces, puede copiar este ejemplo y ejecutarlo tal como está.
Más tarde, para su aplicación de producción, es posible que desee utilizar un servidor de base de datos como PostgreSQL.

## ORMs
FastAPI funciona con cualquier base de datos y cualquier estilo de biblioteca para comunicarse con la base de datos.
Un patrón común es usar un "ORM": una biblioteca de "mapeo relacional de objetos".
Un ORM tiene herramientas para convertir ("mapa") entre objetos en código y tablas de base de datos ("relaciones").
Con un ORM, normalmente creas una clase que representa una tabla en una base de datos SQL, cada atributo de la clase representa una columna, con un nombre y un tipo.
Por ejemplo, una clase Pet podría representar una tabla SQL de mascotas.
Y cada objeto de instancia de esa clase representa una fila en la base de datos.
Por ejemplo, un objeto orion_cat (una instancia de Pet) podría tener un atributo orion_cat.type, para el tipo de columna. Y el valor de ese atributo podría ser, p. "gato".
Estos ORM también cuentan con herramientas para realizar las conexiones o relaciones entre tablas o entidades.
De esta manera, también podría tener un atributo orion_cat.owner y el propietario contendría los datos del propietario de esta mascota, tomados de la tabla de propietarios.
Entonces, orion_cat.owner.name podría ser el nombre (de la columna de nombre en la tabla de propietarios) del dueño de esta mascota.
Podría tener un valor como "Arquilian".
Y el ORM hará todo el trabajo para obtener la información de los propietarios de la tabla correspondiente cuando intente acceder a ella desde su objeto favorito.
Los ORM comunes son, por ejemplo: Django-ORM (parte del marco Django), SQLAlchemy ORM (parte de SQLAlchemy, independiente del marco) y Peewee (independiente del marco), entre otros.
Aquí veremos cómo trabajar con SQLAlchemy ORM.
De manera similar podrías usar cualquier otro ORM.

## File structure
Para estos ejemplos, supongamos que tiene un directorio llamado my_super_project que contiene un subdirectorio llamado sql_app con una estructura como esta:
```
.
└── sql_app
    ├── __init__.py
    ├── crud.py
    ├── database.py
    ├── main.py
    ├── models.py
    └── schemas.py
```

El archivo __init__.py es solo un archivo vacío, pero le dice a Python que sql_app con todos sus módulos (archivos de Python) es un paquete.
Ahora veamos qué hace cada archivo/módulo.

## Crear las partes de SQLAlchemy
Consultemos el archivo sql_app/database.py.

### Importar las partes de SQLAlchemy
```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
```

### Crear una database URL para SQLAlchemy
```
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
```

En este ejemplo, nos estamos "conectando" a una base de datos SQLite (abriendo un archivo con la base de datos SQLite).
El archivo se ubicará en el mismo directorio en el archivo sql_app.db.
Por eso la última parte es ./sql_app.db.
Si estuviera utilizando una base de datos PostgreSQL, solo tendría que descomentar la línea:
```
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
```

...y adáptalo con los datos de tu base de datos y tus credenciales (equivalentemente para MySQL, MariaDB o cualquier otra).

## Crear la SQLAlchemy engine
El primer paso es crear un "motor" de SQLAlchemy.
Más tarde usaremos este motor en otros lugares.
```
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
```

El argumento:
```
connect_args={"check_same_thread": False}
```

... solo se necesita para SQLite. No es necesario para otras bases de datos.

## Crear una SessionLocal class
Cada instancia de la clase SessionLocal será una sesión de base de datos. La clase en sí aún no es una sesión de base de datos.
Pero una vez que creamos una instancia de la clase SessionLocal, esta instancia será la sesión real de la base de datos.
Lo llamamos SessionLocal para distinguirlo de la sesión que estamos importando desde SQLAlchemy.
Usaremos Session (la importada de SQLAlchemy) más adelante.
Para crear la clase SessionLocal, use la función sessionmaker:
```
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

## Crear una Base class
Ahora usaremos la función declarative_base() que devuelve una clase.
Posteriormente heredaremos de esta clase para crear cada uno de los modelos o clases de base de datos (los modelos ORM):
```
Base = declarative_base()
```

## Crear una database models
Ahora veamos el archivo sql_app/models.py.

### Crear modelos de SQLAlchemy a partir de la clase Base
Usaremos esta clase Base que creamos antes para crear los modelos SQLAlchemy.

SQLAlchemy usa el término "modelo" para referirse a estas clases e instancias que interactúan con la base de datos.
Pero Pydantic también usa el término "modelo" para referirse a algo diferente, las clases e instancias de validación, conversión y documentación de datos.

Importar Base desde la base de datos (el archivo base de datos.py de arriba).
Cree clases que hereden de él.
Estas clases son los modelos SQLAlchemy.

```
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")
```

El atributo __tablename__ le dice a SQLAlchemy el nombre de la tabla a usar en la base de datos para cada uno de estos modelos.

## Crear model attributes/columns
Ahora cree todos los atributos del modelo (clase).
Cada uno de estos atributos representa una columna en su tabla de base de datos correspondiente.
Usamos la columna de SQLAlchemy como valor predeterminado.
Y pasamos un "tipo" de clase SQLAlchemy, como Integer, String y Boolean, que define el tipo en la base de datos, como un argumento.
```
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

...
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
```

## Crear las relationships
Ahora crea las relaciones.
Para esto, usamos la relación proporcionada por SQLAlchemy ORM.
Esto se convertirá, más o menos, en un atributo "mágico" que contendrá los valores de otras tablas relacionadas con esta.
```
from sqlalchemy.orm import relationship
...
     items = relationship("Item", back_populates="owner")
...
     owner = relationship("User", back_populates="items")
```

Al acceder a los elementos de atributo en un Usuario, como en my_user.items, tendrá una lista de modelos de Item SQLAlchemy (de la tabla de elementos) que tienen una clave externa que apunta a este registro en la tabla de usuarios.
Cuando accede a my_user.items, SQLAlchemy realmente irá y buscará los elementos de la base de datos en la tabla de elementos y los completará aquí.
Y al acceder al propietario del atributo en un elemento, contendrá un modelo SQLAlchemy de usuario de la tabla de usuarios. Utilizará el atributo/columna owner_id con su clave externa para saber qué registro obtener de la tabla de usuarios.

## Crear los Pydantic models
Ahora revisemos el archivo sql_app/schemas.py.

### Crear initial Pydantic models / schemas
Cree modelos Pydantic ItemBase y UserBase (o digamos "esquemas") para tener atributos comunes al crear o leer datos.
Y cree ItemCreate y UserCreate que hereden de ellos (para que tengan los mismos atributos), además de cualquier dato adicional (atributos) necesarios para la creación.
Así, el usuario también dispondrá de una contraseña a la hora de crearla.
Pero por seguridad, la contraseña no estará en otros modelos de Pydantic, por ejemplo, no se enviará desde la API al leer un usuario.
```
from typing import List, Union
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    class Config:
        orm_mode = True
```

## Estilo SQLAlchemy y estilo Pydantic
Tenga en cuenta que los modelos de SQLAlchemy definen atributos usando = y pasan el tipo como parámetro a Column, como en:
```
name = Column(String)
```

mientras que los modelos Pydantic declaran los tipos usando:, la nueva sintaxis de anotación de tipo/sugerencias de tipo:
```
name: str
```

Téngalo en cuenta, para que no se confunda al usar = y : con ellos.

## Crear modelos Pydantic/esquemas para lectura/retorno
Ahora cree modelos Pydantic (esquemas) que se utilizarán al leer datos, al devolverlos desde la API.
Por ejemplo, antes de crear un artículo, no sabemos cuál será el ID que se le asignará, pero al leerlo (al devolverlo desde la API) ya sabremos su ID.
De la misma manera, al leer un usuario, ahora podemos declarar que los elementos contendrán los elementos que pertenecen a este usuario.
No solo los ID de esos elementos, sino todos los datos que definimos en el modelo de Pydantic para leer elementos: Item.
```
class Item(ItemBase):
    id: int
    owner_id: int

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
```

Tenga en cuenta que el usuario, el modelo de Pydantic que se utilizará al leer un usuario (devolviéndolo desde la API) no incluye la contraseña.

## Use Pydantic's orm_mode
Ahora, en los modelos Pydantic para lectura, Elemento y Usuario, agregue una clase Config interna.
Esta clase Config se usa para proporcionar configuraciones a Pydantic.
En la clase Config, establezca el atributo orm_mode = True.
```
class Config:
        orm_mode = True
```

Observe que está asignando un valor con =, como:
orm_mode = True
No usa : como para las declaraciones de tipos anteriores.
Esto es establecer un valor de configuración, no declarar un tipo.

El orm_mode de Pydantic le indicará al modelo de Pydantic que lea los datos incluso si no es un dict, sino un modelo ORM (o cualquier otro objeto arbitrario con atributos).
De esta manera, en lugar de solo tratar de obtener el valor de identificación de un dictado, como en:
```
id = data["id"]
```

también intentará obtenerlo de un atributo, como en:
```
id = data.id
```

Y con esto, el modelo de Pydantic es compatible con los ORM, y puede simplemente declararlo en el argumento del modelo de respuesta en sus operaciones de ruta.
Podrá devolver un modelo de base de datos y leerá los datos de él.

### Detalles técnicos sobre el modo ORM
SQLAlchemy y muchos otros son por defecto "carga diferida".
Eso significa, por ejemplo, que no obtienen los datos de las relaciones de la base de datos a menos que intente acceder al atributo que contendría esos datos.
Por ejemplo, accediendo a los elementos de atributos:
```
current_user.items
```

haría que SQLAlchemy vaya a la tabla de elementos y obtenga los elementos para este usuario, pero no antes.
Sin orm_mode, si devolviera un modelo SQLAlchemy de su operación de ruta, no incluiría los datos de la relación.
Incluso si declaró esas relaciones en sus modelos Pydantic.
Pero con el modo ORM, como el propio Pydantic intentará acceder a los datos que necesita de los atributos (en lugar de asumir un dict), puede declarar los datos específicos que desea devolver y podrá ir a buscarlos, incluso desde ORM. .



# new