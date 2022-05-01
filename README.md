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
uvicorn main:app --reload
```

### Nota
El comando uvicorn main:app se refiere a:

- main: el archivo main.py (el "módulo" de Python).
- app: el objeto creado dentro de main.py con la línea app = FastAPI().
- --reload: hace que el servidor se reinicie después de cambios en el código. Uso exclusivo para desarrollo.