import cv2
from ultralytics import YOLO

# Load your YOLO model
model = YOLO("best_model.pt")

# Open the video capture or webcam
cap = cv2.VideoCapture(0)  # Use "path/to/video.mp4" for a video file

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference on the frame
    results = model.predict(source=frame, conf=0.55)  # Adjust confidence threshold if needed

    # Display the predictions on the frame
    annotated_frame = results[0].plot()  # Plot the results on the frame
    cv2.imshow("YOLO Detection", annotated_frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()