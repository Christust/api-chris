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



# new