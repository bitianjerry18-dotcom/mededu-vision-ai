from ultralytics import YOLO

# Load model ONCE (important for Render performance)
model = YOLO("models/yolov8n.pt")

def detect_objects(image):
    results = model(image, conf=0.25)

    detections = []

    for r in results:
        for box in r.boxes:
            detections.append({
                "label": model.names[int(box.cls)],
                "confidence": round(float(box.conf), 3)
            })

    return detections
