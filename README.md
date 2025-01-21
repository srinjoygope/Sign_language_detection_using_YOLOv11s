# Sign Language Detection with YOLOv11s

## Overview

This repository contains a project for detecting and recognizing sign language gestures using a YOLOv11s model. The model is trained on a custom dataset containing various sign language gestures, and the project leverages PyTorch and the Ultralytics YOLO library.

## Features

Custom Sign Language Dataset: Includes gestures such as "hello", "thank you", "yes", "no" and "goodbye".

YOLOv11s Model: A state-of-the-art, lightweight object detection model for real-time performance.

Evaluation Metrics: Precision, recall, and mean average precision (mAP) are computed for model evaluation.

Visualization: The training log graph is plotted and also with a normalized confusion matrix for visualizing the accuracy/precision of the results.

## Datasets

The dataset in this project is a custom made image dataset consisting 750 raw images of 640x480 pixel resolution. After that the data is augmented and resized for training purpose.
Following images are a example of the data I used in this work :

![sample image1](sample_data\0e97689a-8f86-4951-869b-f6256a1171e4.jpg)

![sample image2](sample_data\3fae6407-d073-48d4-927e-fbad9f17314d.jpg)

## Installation

1. Clone the repository :

```bash
git clone https://github.com/srinjoygope/Sign_language_detection_using_YOLOv11s

cd Sign_language_detection_using_YOLOv11s
```
2. Run the following command for installing required libraries :

```bash
pip install requirements.txt
```

3. To use the model open code with this command (Your system should have a camera with decent picture quality to do the following action) :

```bash
python use_real_time.py
```

## Real-time demo

![sample image3](results\predictions\0c1e354a-d441-4132-a86e-4fc2a670aba8_jpg.rf.38ee74e6d32a11ac46a844841ed36a49.jpg)

![sample image4](results\predictions\35d57e0b-3a3e-4922-b62b-b9d6e4f7b617_jpg.rf.3abc0d01e66393544d854c4d3d1d4c2d.jpg)

![sample image5](results\predictions\40f98cd6-1df2-48dc-8e8c-5725ada43307_jpg.rf.2465fe1ae0feea8052c547d8cf93c463.jpg)

## Results

| Class       | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|-------------|-----------|--------|---------|--------------|
| Goodbye     | 0.997     | 1.000  | 0.995   | 0.935        |
| Hello       | 0.997     | 1.000  | 0.995   | 0.953        |
| No          | 1.000     | 1.000  | 0.995   | 0.866        |
| Thank You   | 1.000     | 1.000  | 0.995   | 0.843        |
| Yes         | 0.998     | 1.000  | 0.995   | 0.876        |


## Future work

In future I would like to add around 30 to 50 words of sign language so that I can further update the code as it can generate a complete sentence of what the person is telling through sign language. It will help in many virtual fields like online meetings via a conference video call.

## Acknowledgements

Ultralytics YOLO: For the robust object detection framework.

PyTorch: For providing the underlying deep learning infrastructure.

## Licence

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Srinjoy Gope