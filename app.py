import os
from flask import Flask, render_template

# Import dlib only if needed (e.g., for face detection)
# import dlib

app = Flask(__name__)

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the shape predictor model file
model_file = os.path.join(current_dir, 'shape_predictor_68_face_landmarks.dat')

# Load the shape predictor model if needed
# predictor = dlib.shape_predictor(model_file)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
