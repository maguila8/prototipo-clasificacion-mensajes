# Prototipo de clasificación de mensajes

## Descripción

Este proyecto consiste en un prototipo de clasificación automática de mensajes de atención al cliente mediante Machine Learning.

Se utiliza un modelo de Regresión Logística entrenado con un conjunto de datos público. La aplicación permite recibir mensajes mediante una API desarrollada con FastAPI y predecir su categoría.

El proyecto está contenerizado con Docker para facilitar su ejecución en diferentes entornos.

## Tecnologías utilizadas

- Python
- Scikit-learn
- TF-IDF
- Regresión Logística
- FastAPI
- Docker

## Estructura del proyecto

- `app/`: código de la API.
- `modelo/`: modelo de clasificación entrenado.
- `documentacion/`: manual de despliegue.
- `pruebas/`: resultados de las pruebas.
- `Dockerfile`: instrucciones para construir la imagen.
- `requirements.txt`: dependencias del proyecto.

## Ejecución con Docker

Construir la imagen:

```bash
docker build -t clasificador-mensajes .
```

Ejecutar el contenedor:

```bash
docker run -d --name clasificador-api -p 8000:8000 clasificador-mensajes
```

Abrir la documentación interactiva de la API:

`http://localhost:8000/docs`

## Alcance y limitaciones

El prototipo fue desarrollado y validado utilizando un conjunto de datos público de mensajes de atención al cliente. Su finalidad es demostrar la integración de un modelo de Machine Learning con una API y Docker.

Para su implementación en un entorno empresarial sería necesario entrenar y evaluar el modelo con correos reales autorizados, así como revisar su desempeño en el contexto específico de la organización.
