This system uses YOLOv8 object detection combined with OpenCV to monitor and analyze live traffic feeds. It automates traffic signal control, detects accidents, identifies vehicles by speed, number plate, and color — all in real time.
**Features**
Feature
**Description**
**Vehicle Detection & Counting**
Detects and counts vehicles per lane using YOLOv8
**Traffic Signal Automation**
Dynamically adjusts signal timing based on vehicle density
**Accident Detection**
Flags unusual motion patterns indicating accidents
**Speed Detection**
Estimates vehicle speed using frame-to-frame displacement
**Number Plate Recognition**
Extracts license plate text using EasyOCR
**Vehicle Color Detection**
Identifies vehicle color via HSV color segmentation
**Web Dashboard**
Flask-based live monitoring dashboard with logs
**Tech Stack**
Language: Python 3.8+
Object Detection: YOLOv8 (Ultralytics)
Computer Vision: OpenCV 4.8.0.76
OCR: EasyOCR
Web Framework: Flask
Database: SQLite / MySQL
Numerical Processing: NumPy 1.26.4
