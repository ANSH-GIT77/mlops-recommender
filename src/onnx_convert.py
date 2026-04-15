import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import numpy as np

# Load processed data
data = pd.read_csv("data/processed_data.csv")

# Convert interaction to numeric
interaction_map = {
    "view": 0,
    "click": 1,
    "purchase": 2
}

data["label"] = data["interaction"].map(interaction_map)

# Simple features (for demo model)
X = data[["user_id", "product_id"]]
y = data["label"]

# Train simple model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

print("Model trained successfully!")

# Convert to ONNX
initial_type = [('float_input', FloatTensorType([None, 2]))]

onnx_model = convert_sklearn(model, initial_types=initial_type)

# Save ONNX model
with open("models/model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("ONNX model saved at models/model.onnx")