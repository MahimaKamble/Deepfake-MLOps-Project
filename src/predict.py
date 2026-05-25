import joblib
import numpy as np
import os

from preprocess import preprocess_image
from feature_extraction import extract_features
from handcrafted_features import extract_handcrafted_features


# Base directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Model path
MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "densenet121_knn_final.pkl"
)

# Load trained KNN model
model = joblib.load(MODEL_PATH)


def predict_image(image_path):

    # Step 1: preprocess image
    img = preprocess_image(image_path)

    # Step 2: deep features
    deep_features = extract_features(img)

    # Step 3: handcrafted features
    handcrafted_features = extract_handcrafted_features(img)

    # Step 4: flatten deep features
    deep_features = deep_features.flatten()

    # Step 5: combine features
    final_features = np.concatenate([
        deep_features,
        handcrafted_features
    ])

    # Step 6: reshape for prediction
    final_features = final_features.reshape(1, -1)

    # Step 7: prediction
    prediction = model.predict(final_features)

    # Step 8: return label
    if prediction[0] == 0:
      return "REAL"
    else:
      return "FAKE"