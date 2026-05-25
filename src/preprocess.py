import cv2
import numpy as np

IMG_SIZE = 224

def preprocess_image(image_path):

    img = cv2.imread(image_path)

    # Convert BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize image
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

    # Convert datatype
    img = img.astype(np.float32)

    return img