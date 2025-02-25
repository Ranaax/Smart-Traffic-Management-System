import os

# KITTI and YOLO format classes
CLASS_MAPPING = {
    "Car": 0, "Van": 1, "Truck": 2, "Pedestrian": 3, "Person_sitting": 4,
    "Cyclist": 5, "Tram": 6, "Misc": 7, "DontCare": 8
}

def convert_kitti_to_yolo(kitti_labels_dir, yolo_labels_dir, image_width=1242, image_height=375):
    """ Converts KITTI label format to YOLO format and saves new labels. """
    
    if not os.path.exists(yolo_labels_dir):
        os.makedirs(yolo_labels_dir)
    
    for filename in os.listdir(kitti_labels_dir):
        if not filename.endswith(".txt"):
            continue
        
        kitti_label_path = os.path.join(kitti_labels_dir, filename)
        yolo_label_path = os.path.join(yolo_labels_dir, filename)
        
        with open(kitti_label_path, "r") as file:
            lines = file.readlines()
        
        yolo_lines = []
        for line in lines:
            data = line.split()
            obj_class = data[0]
            
            if obj_class not in CLASS_MAPPING:
                continue
            
            x_min, y_min, x_max, y_max = map(float, data[4:8])
            
            # Convert to YOLO format
            x_center = ((x_min + x_max) / 2) / image_width
            y_center = ((y_min + y_max) / 2) / image_height
            bbox_width = (x_max - x_min) / image_width
            bbox_height = (y_max - y_min) / image_height
            
            yolo_lines.append(f"{CLASS_MAPPING[obj_class]} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}")
        
        with open(yolo_label_path, "w") as yolo_file:
            yolo_file.write("\n".join(yolo_lines))
    
    print(f"Conversion completed! YOLO labels saved in '{yolo_labels_dir}'")

# Run conversion
convert_kitti_to_yolo("data/labels_kitti", "data/labels_yolo")
