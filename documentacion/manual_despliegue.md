# Manual de despliegue del prototipo de clasificación de mensajes

## 1. Descripción del proyecto

Este proyecto consiste en un prototipo de clasificación automática de mensajes de atención al cliente mediante un modelo de Machine Learning.

La aplicación utiliza un modelo de Regresión Logística previamente entrenado, integrado mediante una API desarrollada con FastAPI y empaquetado en un contenedor Docker.

El objetivo es facilitar su ejecución y permitir su posterior despliegue en un entorno de nube.

## 2. Requisitos técnicos

Para ejecutar el proyecto se necesitan los siguientes componentes:

- Python 3.12 o compatible.
- Docker Desktop o Docker Engine.
- Una cuenta de GitHub para acceder al código fuente.
- Conexión a internet para descargar las imágenes y dependencias necesarias.

## 3. Estructura del proyecto

El repositorio contiene los siguientes archivos:

- `app/main.py`: código de la API y conexión con el modelo.
- `modelo/modelo_regresion_logistica.joblib`: modelo entrenado.
- `Dockerfile`: instrucciones para construir la imagen.
- `requirements.txt`: librerías necesarias.
- `README.md`: descripción general del proyecto.

## 4. Construcción de la imagen Docker

Una vez descargado el repositorio y abierto el directorio principal del proyecto, se ejecuta el siguiente comando:

```bash
docker build -t clasificador-mensajes .
```

Este comando construye una imagen que contiene la aplicación, el modelo entrenado y las dependencias necesarias para su funcionamiento.

## 5. Ejecución del contenedor

Para iniciar la aplicación se utiliza:

```bash
docker run -d --name clasificador-api -p 8000:8000 clasificador-mensajes
```

El contenedor ejecuta la API y permite acceder a ella mediante el puerto 8000.

Para consultar la documentación interactiva y probar los endpoints, se ingresa a:

`http://localhost:8000/docs`

## 6. Validación del funcionamiento

Se debe comprobar que la API responda correctamente y que el endpoint `POST /predecir` pueda recibir mensajes y devolver una categoría.

También se deben probar entradas vacías y campos obligatorios faltantes para verificar el manejo de errores.

## 7. Estrategia de despliegue en la nube

Se propone utilizar un servicio de nube compatible con contenedores Docker, como una plataforma PaaS o un servicio de ejecución de contenedores.

La estrategia propuesta consiste en:

1. Mantener el código fuente y los archivos del modelo en el repositorio de GitHub.
2. Crear un servicio de aplicación en la plataforma de nube seleccionada.
3. Conectar el servicio con el repositorio de GitHub.
4. Seleccionar la opción de construcción mediante Dockerfile.
5. Configurar el puerto 8000 para permitir la comunicación con la API.
6. Ejecutar el proceso de construcción y despliegue.
7. Obtener la dirección pública de la aplicación.
8. Acceder a la ruta `/docs` para comprobar que la API esté disponible.
9. Realizar pruebas de clasificación desde el entorno desplegado.

## 8. Consideraciones para una implementación empresarial

El prototipo fue desarrollado y probado utilizando un conjunto de datos público de mensajes de atención al cliente.

Para utilizarlo en un entorno empresarial sería necesario evaluar el modelo con correos reales autorizados, revisar las categorías requeridas y ajustar su entrenamiento según las características de los mensajes de la organización.

También sería importante proteger la información confidencial, controlar el acceso a la API y monitorear su funcionamiento.

## 9. Estado del despliegue

La aplicación fue ejecutada y validada localmente mediante Docker. El despliegue en la nube se plantea como una estrategia de implementación posterior y todavía no se ha realizado.
