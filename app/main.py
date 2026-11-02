#importar las librerías necesarias
from pathlib import Path
import joblib

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#obtener la ubicación del proyecto
RUTA_PROYECTO = Path(__file__).resolve().parent.parent
RUTA_MODELO = RUTA_PROYECTO / "modelo" / "modelo_regresion_logistica.joblib"

#cargar el modelo entrenado
modelo = joblib.load(RUTA_MODELO)

#crear la aplicación
app = FastAPI(
    title="Clasificador de Mensajes",
    description="API para clasificar mensajes de atención al cliente",
    version="1.0.0"
)

#definir los datos que recibirá la API
class Mensaje(BaseModel):
    asunto: str = ""
    cuerpo: str

#endpoint para comprobar que la API funciona
@app.get("/")
def inicio():
    return {"mensaje": "API de clasificación funcionando correctamente"}

#endpoint para clasificar mensajes
@app.post("/predecir")
def predecir(mensaje: Mensaje):

    #unir el asunto y el cuerpo del mensaje
    texto = f"{mensaje.asunto} {mensaje.cuerpo}".strip()

    #validar que exista texto
    if not texto:
        raise HTTPException(
            status_code=400,
            detail="El mensaje no puede estar vacío"
        )

    #realizar la predicción
    categoria = modelo.predict([texto])[0]

    #obtener la probabilidad más alta
    probabilidades = modelo.predict_proba([texto])[0]
    probabilidad = float(max(probabilidades))

    #devolver el resultado
    return {
        "categoria_predicha": str(categoria),
        "probabilidad": round(probabilidad, 4)
    }
