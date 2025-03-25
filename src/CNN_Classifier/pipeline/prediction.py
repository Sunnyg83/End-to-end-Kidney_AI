import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename
        # Update the path to the correct location of model.h5
        self.model_path = os.path.join("artifacts", "training", "model.h5")
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"The model file was not found at {self.model_path}. Please ensure the file exists.")
        self.model = load_model(self.model_path)




    
    def predict(self):
        # load model
        model = load_model(os.path.join("model", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        # change to a numpy array
        test_image = np.expand_dims(test_image, axis = 0)
        # expand the dimension
        result = np.argmax(model.predict(test_image), axis=1)
        # the line above returns the index of the class with the highest probability (sofmax)
        print(result)
        # model outputs 2 values: probability it is normal and probability it is tumor
        # if the first value is higher than the second, then it is normal
        # if the second value is higher than the first, then it is tumor
        # it is stored in  a 1D array of size two, and the index of the highest value determines tumor or normal

        if result[0] == 1:
            prediction = 'Kidney Tumor'
            return [{ "AI prediction" : prediction}]
        else:
            prediction = 'No Kidney Tumor'
            return [{ "AI prediction" : prediction}]