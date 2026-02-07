from pydantic import BaseModel, Field
from typing import List

class PredictRequest(BaseModel):
    features: List[float] = Field(..., min_length=4, max_length=4)

class PredictResponse(BaseModel):
    predicted_class: int
    class_probabilities: List[float]
    model_version: str
