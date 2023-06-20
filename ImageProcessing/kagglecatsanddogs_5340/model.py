import cv2
import sys
import numpy as np
import tflite_runtime.interpreter as tflite

def preprocess_image(image, input_shape):
    resized_image = cv2.resize(image, (input_shape[1], input_shape[2]))
    grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    normalized_image = grayscale_image.astype(np.float32) / 255.0
    reshaped_image = np.reshape(normalized_image, input_shape)
    return reshaped_image

# Define the class labels or mapping
class_labels = ["Dog", "Cat"]  # Replace with your class labels

# Load the TensorFlow Lite model
interpreter = tflite.Interpreter(model_path='/home/filippaliuc/Desktop/Programare/PetRecognition/converted_tflite_1000/vww_96_grayscale_quantized.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Get the input shape of the model
input_shape = input_details[0]['shape']

# Load and preprocess the local photo image
if len(sys.argv) < 2:
    print("Please provide the image path as a command-line argument.")
    sys.exit(1)

image_path = sys.argv[1]
image = cv2.imread(image_path)

# Preprocess the image
input_data = preprocess_image(image, input_shape)

# Set the input tensor
interpreter.set_tensor(input_details[0]['index'], input_data)

# Perform inference using the TensorFlow Lite model
interpreter.invoke()

# Get the output tensor
output_data = interpreter.get_tensor(output_details[0]['index'])

# Postprocess the output data as needed

# Get the predicted class label
predicted_class_index = np.argmax(output_data)
predicted_class_label = class_labels[predicted_class_index]

# Print the predicted class
print(output_data)
print("Predicted Class:", predicted_class_label)

# Display the results or perform actions based on the predictions

# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
