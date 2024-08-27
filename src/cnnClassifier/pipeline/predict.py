import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts","training", "model.keras"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 0:
            prediction = '0-24'
            return [{ "image" : prediction}]
        elif result[0] == 1:
            prediction = '25-49'
            return [{ "image" : prediction}]
        elif result[0] == 2:
            prediction = '50-74'
            return [{ "image" : prediction}]
        elif result[0] == 3:
            prediction = '75-99'
            return [{ "image" : prediction}]
        else:
            prediction = '100-124'
            return [{ "image" : prediction}]
        
    
    
