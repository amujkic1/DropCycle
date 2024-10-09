from flask import Flask, render_template, jsonify
from imagedet import CLIENT

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/api/sort-garbage', methods=['POST'])
def sort_garbage():
    print("sorting")
    # instead of hardcoding the image use the one from html formData
    result = CLIENT.infer(r"C:\Users\HP\Desktop\DropCycle_img\apples.jpg", model_id="yolo-waste-detection/1")
    detected_class = result['predictions'][0]['class']
    return jsonify({'type': detected_class})

if __name__ == '__main__':
    app.run()
    