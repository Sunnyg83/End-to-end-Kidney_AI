# using flask to make an api

import base64
from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from CNN_Classifier.utils.common import decodeImage
# image should be decoded into a base 64 string
# this is done in the decodeImage function
# encode it in base 64 then decode it to get the image
from CNN_Classifier.pipeline.prediction import PredictionPipeline



os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        # whatever image the user sends will be saved as inputImage
        self.classifier = PredictionPipeline(self.filename)
        # Prediction pipeline takes one argument, the filename of the image


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')




@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    # os.system("dvc repro")
    return "Training done successfully!"



@app.route("/predict", methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'image' not in data:
            return jsonify({"error": "No image data provided"}), 400

        image_data = data['image']
        image_path = "temp_image.jpg"
        with open(image_path, "wb") as f:
            f.write(base64.b64decode(image_data))

        pipeline = PredictionPipeline(image_path)
        result = pipeline.predict()
        return jsonify(result)

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    clApp = ClientApp()

    app.run(host='0.0.0.0', port=8080) #for AWS