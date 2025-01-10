import cv2
from detect_objects import detect_objects

object_subobject_mapping = {
    "Person": ["Helmet", "Bag", "Shoes"],
    "Car": ["Tire", "Door", "Window"]
}

def assign_subobjects(objects_detected, class_ids):
    object_hierarchy = []
    for i, object_name in enumerate(objects_detected):
        subobjects = object_subobject_mapping.get(object_name, [])
        subobject_data = []
        
        for subobject in subobjects:
            subobject_data.append({
                "object": subobject,
                "id": i + 1,
                "bbox": [100, 100, 150, 150]  
            })
        
        object_hierarchy.append({
            "object": object_name,
            "id": i + 1,
            "bbox": [50, 50, 200, 200], 
            "subobject": subobject_data
        })
    
    return object_hierarchy

def save_subobject_image(frame, bbox, subobject_name, object_id):
    x, y, w, h = bbox
    subobject_image = frame[y:y+h, x:x+w]
    cv2.imwrite(f"subobject_{subobject_name}_object_{object_id}.jpg", subobject_image)
