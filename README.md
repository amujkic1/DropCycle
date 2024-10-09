# DropCycle

This Python application recognizes different types of waste (e.g., plastic bottles, glass, etc.) using an external API. The app allows users to upload or capture images, processes them through the API, and returns the type of waste detected. The app also provides recycling tips based on the recognized type and maintains a history of classifications for future reference.

## Features

- **Image Upload**: Uploading images of garbage for classification.
- **AI Integration**: Garbage recognition API used to detect types of garbage (plastic, glass, etc.).
- **Result Display**: Showing recognized garbage types along with recycling tips.
- **Classification History**: Keeping a log of past classifications.

This app uses the [Waste Detection API](https://universe.roboflow.com/projectverba/yolo-waste-detection/model/1) to classify waste types based on uploaded or captured images. The API processes the image and returns the identified garbage type such as plastic bottles, glass, paper, etc.
