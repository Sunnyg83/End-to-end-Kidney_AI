import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        # Update the path to the correct location of model.h5
        self.model_path = os.path.join("artifacts", "training", "model.h5")
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"The model file was not found at {self.model_path}. Please ensure the file exists.")
        
        # Load model
        self.model = load_model(self.model_path)
        print(f"Model loaded successfully from {self.model_path}")
    
    def predict(self):
        try:
            # Use the model loaded in __init__
            imagename = self.filename
            print(f"Processing image: {imagename}")
            
            # Load and preprocess image
            test_image = image.load_img(imagename, target_size=(224, 224))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            test_image = test_image / 255.0  # Normalize the image
            
            # Get predictions
            predictions = self.model.predict(test_image, verbose=0)
            
            # Get the predicted class
            result = np.argmax(predictions, axis=1)
            
            # Determine prediction
            if result[0] == 1:
                prediction = 'Tumor'
            else:
                prediction = 'Normal'
            
            print(f"Final prediction: {prediction}")
            
            return [{"AI prediction": prediction}]
            
        except Exception as e:
            print("Error during prediction:", str(e))
            return [{"image": "Error occurred during prediction"}]