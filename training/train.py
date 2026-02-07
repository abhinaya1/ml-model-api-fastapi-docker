import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# 1) Load data
iris = load_iris()
X, y = iris.data, iris.target  # 4 numeric features

# 2) Build pipeline (preprocess + model together)
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=200))
])

# 3) Train
pipeline.fit(X, y)

# 4) Save
joblib.dump(pipeline, "../serving/model/model.joblib")
print("Saved model.joblib")
