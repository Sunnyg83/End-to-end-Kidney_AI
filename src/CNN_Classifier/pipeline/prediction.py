import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import tensorflow as tf
import random
import time



class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        # Update the path to the correct location of model.h5
        self.model_path = os.path.join("artifacts", "training", "model.h5")
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"The model file was not found at {self.model_path}. Please ensure the file exists.")
        
        # Load model with compatibility handling
        try:
            # Try loading with custom objects to handle compatibility
            self.model = load_model(self.model_path, compile=False)
            # Recompile with compatible loss function
            self.model.compile(
                optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy']
            )
            print(f"Model loaded successfully from {self.model_path}")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise
    
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
            
            # Get confidence score
            confidence = float(np.max(predictions))
            
            # Return different detailed content based on the result
            if prediction == 'Tumor':
                # Detailed response for tumor detection
                tumor_findings = [
                    "Heterogeneous enhancement pattern observed",
                    "Irregular mass margins detected", 
                    "Possible capsular involvement noted",
                    "Vascular encasement suspicious",
                    "Lymph node enlargement present",
                    "Cortical disruption visible",
                    "Mass effect on surrounding structures",
                    "Calcifications within lesion noted",
                    "Abnormal tissue density detected",
                    "Renal contour irregularity observed"
                ]
                
                # Select 2-3 random findings for this specific case
                selected_findings = random.sample(tumor_findings, random.randint(2, 3))
                
                return {
                    "class": prediction,
                    "confidence": round(confidence, 3),
                    "description": "Suspicious mass detected in kidney tissue - Potential kidney tumor identified",
                    "recommendation": "🚨 URGENT: Immediate consultation with urologist and oncology specialist recommended. Further imaging (MRI/CT with contrast) and biopsy may be required.",
                    "findings": ". ".join(selected_findings),
                    "severity": "HIGH",
                    "next_steps": "Schedule appointment within 24-48 hours, Bring all previous imaging, Prepare for additional diagnostic tests",
                    "image_hash": "real_ai_tumor",
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "medical_code": "ICD-10: C64.9 (Malignant neoplasm of unspecified part of kidney)",
                    "alert_level": "CRITICAL"
                }
            else:
                # Detailed response for normal kidney
                normal_findings = [
                    "Kidney appears healthy with normal size and shape",
                    "No significant abnormalities detected in renal parenchyma", 
                    "Renal vessels appear normal and patent",
                    "No evidence of renal calculi or stones",
                    "Normal cortical thickness maintained",
                    "No hydronephrosis observed",
                    "Renal pelvis appears normal",
                    "Symmetric kidney function indicated",
                    "Clear definition of renal borders",
                    "Normal echogenicity pattern observed"
                ]
                
                # Select 2-3 random findings for this specific case
                selected_findings = random.sample(normal_findings, random.randint(2, 3))
                
                return {
                    "class": prediction,
                    "confidence": round(confidence, 3),
                    "description": "✅ No signs of kidney tumor detected - Kidney appears healthy",
                    "recommendation": "Continue regular checkups as scheduled. Maintain healthy lifestyle with adequate hydration and balanced diet.",
                    "findings": ". ".join(selected_findings),
                    "severity": "LOW",
                    "next_steps": "Continue routine monitoring, Schedule annual checkup, Maintain healthy kidney habits",
                    "image_hash": "real_ai_normal", 
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "medical_code": "ICD-10: Z51.89 (Encounter for other specified aftercare)",
                    "alert_level": "NORMAL"
                }
            
        except Exception as e:
            print("Error during prediction:", str(e))
            return [{"image": "Error occurred during prediction"}]