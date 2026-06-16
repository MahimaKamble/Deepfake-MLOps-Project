from flask import Flask, render_template, request
import os

from predict import predict_image

import mlflow
import mlflow.sklearn
import webbrowser

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


# MLflow setup
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Deepfake_Detection")


# Upload foldere3
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "static"
)

# Create static folder automatically
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():

    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    # Check if file exists
    if 'file' not in request.files:

        return render_template(
            "index.html",
            prediction="No file uploaded",
            image_file=None
        )

    file = request.files['file']

    # Check empty filename
    if file.filename == '':

        return render_template(
            "index.html",
            prediction="Please choose an image",
            image_file=None
        )

    # Save uploaded file
    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(filepath)

    # Prediction
    result = predict_image(filepath)

    # MLflow logging
    with mlflow.start_run():

        mlflow.log_param("filename", file.filename)

        mlflow.log_param("prediction", result)

        # Log metrics
        if result == "REAL":
            mlflow.log_metric("real_count", 1)
            mlflow.log_metric("fake_count", 0)

        else:
            mlflow.log_metric("real_count", 0)
            mlflow.log_metric("fake_count", 1)

    # Return result
    return render_template(
        "index.html",
        prediction=result,
        image_file=file.filename
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

   # webhook test 
   # webhook working test
   # automatic trigger test
   # polling test
   #Final test
   # Test