import os
from dotenv import load_dotenv
from inference_sdk import InferenceHTTPClient

load_dotenv()

api_key = os.getenv("API_KEY")

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=api_key
)

result = CLIENT.infer(r"C:\Users\HP\Desktop\DropCycle_img\apples.jpg", model_id="yolo-waste-detection/1")
print(result)
