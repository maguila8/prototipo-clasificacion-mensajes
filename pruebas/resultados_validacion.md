# Resultados de pruebas y validación

## 1. Objetivo

Comprobar el funcionamiento de la API de clasificación de mensajes y verificar que el modelo integrado pueda procesar diferentes entradas y responder correctamente ante situaciones esperadas y casos límite.

## 2. Entorno de pruebas

Las pruebas se realizaron utilizando:

- Modelo: Regresión Logística.
- Representación de texto: TF-IDF.
- API: FastAPI.
- Contenedor: Docker.
- Endpoint de clasificación: `POST /predecir`.
- Entorno: ejecución local mediante Docker Desktop.

## 3. Pruebas funcionales y casos límite

| Caso de prueba | Entrada | Resultado obtenido | Estado |
|---|---|---|---|
| Mensaje de pedido | "I want to know the status of my order" | ORDER (0.7343) | Correcto |
| Mensaje de reembolso | "I want to get my money back because the product was damaged" | REFUND (0.9934) | Correcto |
| Mensaje sin asunto | "I want to know where my package is" | DELIVERY (0.3766) | Correcto |
| Mensaje completamente vacío | Asunto y cuerpo vacíos | HTTP 400 | Correcto |
| Falta el campo cuerpo | Solo se proporciona el asunto | HTTP 422 | Correcto |

## 4. Análisis de resultados

La API procesó correctamente los mensajes de prueba y devolvió las categorías correspondientes. También respondió adecuadamente ante entradas vacías y campos obligatorios faltantes.

Se observó que la predicción de algunos mensajes puede presentar una probabilidad baja. Por ejemplo, el mensaje sin asunto obtuvo una probabilidad de 0.3766. Esto indica que, aunque el modelo puede devolver una categoría, no todas las predicciones tienen el mismo nivel de confianza.

## 5. Validación mediante Docker

Se construyó la imagen Docker del proyecto y se ejecutó un contenedor utilizando el puerto 8000.

Posteriormente, se accedió a la documentación interactiva de FastAPI mediante `http://localhost:8000/docs` y se realizaron pruebas con el endpoint de clasificación.

Los resultados confirmaron que el modelo pudo realizar predicciones desde el contenedor, sin necesidad de ejecutar la API directamente desde el entorno local de Python.

## 6. Limitaciones identificadas

- El modelo fue entrenado con un conjunto de datos público de atención al cliente.
- Las categorías actuales no necesariamente representan las necesidades de una empresa.
- Las probabilidades devueltas no deben interpretarse como una certeza de que la categoría sea correcta.
- Es necesario evaluar el modelo con correos reales autorizados antes de utilizarlo en un entorno empresarial.

## 7. Conclusión

Las pruebas permitieron comprobar la integración entre el modelo de Machine Learning, la API desarrollada con FastAPI y Docker.

El prototipo funciona correctamente en el entorno local y demuestra que es posible utilizar un modelo entrenado mediante un servicio de clasificación accesible a través de una API.

Como siguiente etapa, se propone evaluar el sistema con datos reales autorizados y realizar su despliegue en la nube.
