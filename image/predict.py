from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np
from PIL import Image
from io import BytesIO
from model import get_model

model = get_model()

def get_label(num):
    label_map = {
        0: 'cardboard',
        1: 'glass',
        2: 'metal',
        3: 'paper', 
        4: 'plastic',
        5: 'trash'
    }
    return label_map[num]

def read_image(file) -> Image.Image:
    pil_image = Image.open(BytesIO(file))
    # pil_image = Image.open(file)
    return pil_image

def transform(file: Image.Image):
    img = np.asarray(file.resize((300, 300)))[..., :3]
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    label = get_label(preds.argmax())
    print('Prediction:', preds)
    print('label:', label)
    return label

if __name__ == "__main__":
    img = read_image("./image/cardboard.jpg")
    preds = transform(img)
    print(preds)