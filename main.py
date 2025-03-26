import tensorflow as tf
from flask import Flask, jsonify, request
import keras

# Initialize the flask application
app = Flask(__name__)

# Load the model
try:
    model = keras.models.load_model('cifar10_tl.keras')
    class_names =['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog',
              'frog', 'horse', 'ship', 'truck']
except Exception as e:
    raise RuntimeError(f"Failed to load model: {str(e)}") from e

# Preprocess image
def preprocess_image(image):
    image = tf.image.resize(image, (224, 224)) # Resize
    image = keras.applications.resnet50.preprocess_input(image) # Normalize using ResNet50's preprocessing
    return image

result = dict()

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    file = request.files['file']
    img_bytes = file.read() # Read the image data as bytes

    # Convert bytes to tensor
    img = tf.io.decode_image(img_bytes, channels=3)

    # Preprocess the image
    img = preprocess_image(img)

    # Add batch dimensions (tensorflow expects a batch) to make shape (1, 224, 224, 3)
    img = tf.expand_dims(img, axis=0)

    # Make predictions with the model
    predictions = model.predict(img)

    for pred, pred_class in zip(predictions[0], class_names):
        print(pred, pred_class) # debug
        result[pred_class] = float(pred)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


