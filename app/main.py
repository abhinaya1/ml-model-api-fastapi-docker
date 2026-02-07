import numpy as np
from fastapi import FastAPI
from app.schemas import PredictRequest, PredictResponse
from app.model import load_model, load_metadata

app = FastAPI(title="Iris Model API", version="1.0.0")

model = load_model()
meta = load_metadata()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return meta

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    X = np.array(req.features, dtype=float).reshape(1, -1)
    pred = int(model.predict(X)[0])
    proba = model.predict_proba(X)[0].tolist()

    return PredictResponse(
        predicted_class=pred,
        class_probabilities=proba,
        model_version=meta.get("model_version", "unknown"),
    )
