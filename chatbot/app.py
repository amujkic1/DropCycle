from flask import Flask, render_template, jsonify, request
from imagedet import CLIENT
import os

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# Create a directory to save uploaded images
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/api/sort-garbage', methods=['POST'])
def sort_garbage():

    if 'image' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    
    # Save the file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    print("sorting")
    # instead of hardcoding the image use the one from html formData
    result = CLIENT.infer(file_path, model_id="yolo-waste-detection/1")
    detected_class = result['predictions'][0]['class']
    
    return jsonify({'type': detected_class})

if __name__ == '__main__':
    app.run()
    