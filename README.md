# Smart-Traffic-Management-System

🚦An AI-powered Smart Traffic Management System utilizing YOLO and DeepSORT for real-time vehicle detection and tracking.


## Features  
- Uses YOLO and DeepSORT for object detection and tracking  
- Improves traffic flow with real-time analysis  
- Works with KITTI and COCO datasets  

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Ranaax/Smart-Traffic-Management-System.git
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the system:
   ```bash
   python main.py

## Demo result 
![detecting and tracking cars](results/DemoVideo.mp4)


## Dataset

This project uses the KITTI Object Detection Dataset.

🔗 **Download Links:**  
- [Left color images (12GB)](https://www.cvlibs.net/download.php?file=data_object_image_2.zip)  
- [Training labels (5MB)](https://www.cvlibs.net/download.php?file=data_object_label_2.zip)

### 📂 Dataset Folder Structure  
Once downloaded, organize the dataset as follows:

data/ │── images/ # Left color images (12GB) │── labels/ # Training labels (5MB, converted to YOLO format)


### 🔄 Label Conversion
The original KITTI labels are in `.txt` files with bounding box details. They must be converted to YOLO format before training.  
A conversion script is provided in `convert_kitti_to_yolo.py`.

