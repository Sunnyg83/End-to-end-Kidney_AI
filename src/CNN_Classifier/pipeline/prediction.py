import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
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
            prediction = 'The AI predicts a Kidney Tumor from the CT Scan'
            return [{ "image" : prediction}]
        else:
            prediction = 'The AI predicts a Normal Tumor from the CT Scan!'
            return [{ "image" : prediction}]