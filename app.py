from fastapi import FastAPI, Request
import uvicorn
import os
from src.textSummarizer.pipeline.prediction import PredictionPipeline
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", tags=["authentication"])
async def index():
    return {"message": "Hello World"}

@app.post("/train")
async def training():
    os.system("python main.py")
    return {"message": "Training Successful"}

@app.post("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        result = obj.predict(text)
        return {"summary": result}
    except Exception as e:
        return {"error": str(e)}
