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

## Primeros pasos
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
...

```