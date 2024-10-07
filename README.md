# DropCycle

This Python application recognizes different types of garbage (e.g., plastic bottles, glass, etc.) using an external API. The app allows users to upload or capture images, processes them through the API, and returns the type of garbage detected. The app also provides recycling tips based on the recognized type and maintains a history of classifications for future reference.

## Features

- **Image Upload**: Upload images of garbage for classification.
- **API Integration**: Use the garbage recognition API to detect types of garbage (plastic, glass, etc.).
- **Result Display**: Show recognized garbage types along with recycling tips.
- **Classification History**: Keep a log of past classifications.

This app uses the [Garbage Recognition API](https://universe.roboflow.com/projectverba/yolo-waste-detection/model/1) to classify garbage types based on uploaded or captured images. The API processes the image and returns the identified garbage type such as plastic bottles, glass, paper, etc.
