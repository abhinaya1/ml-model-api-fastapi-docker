import json
import joblib
from pathlib import Path

MODEL_PATH = Path("model/model.joblib")
META_PATH = Path("model/metadata.json")

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Missing model file: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)

def load_metadata():
    if META_PATH.exists():
        return json.loads(META_PATH.read_text())
    return {"model_version": "unknown"}
