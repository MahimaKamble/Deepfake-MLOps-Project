import numpy as np

from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.applications.densenet import preprocess_input


base_model = DenseNet121(
    weights='imagenet',
    include_top=False,
    pooling='avg'
)


def extract_features(img):

    img = np.expand_dims(img, axis=0)

    # ONLY preprocessing needed
    img = preprocess_input(img)

    features = base_model.predict(img)

    return features