import cv2
import os

def capture_images_from_camera(output_directory):
    os.makedirs(output_directory, exist_ok=True)
    existing_images = os.listdir(output_directory)
    img_counter = len(existing_images)

    # Load the Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cam = cv2.VideoCapture(0)

    capture_photo = False  # Flag to indicate when to capture a photo

    while True:
        # Capture the frame from the camera
        ret, frame = cam.read()

        # Verify if the frame is captured
        if not ret:
            print('Error al capturar el frame')
            break

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if capture_photo:
            capture_photo = False  # Reset the capture_photo flag

            # Save the picture without displaying the green rectangle
            img_name = f'selfie_{img_counter}.png'
            img_path = os.path.join(output_directory, img_name)
            cv2.imwrite(img_path, frame)
            print(f'Imagen guardada en: {img_path}')

            # Increase the counter
            img_counter += 1

        else:
            # Draw rectangles around the detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Show the frame in a window
        cv2.imshow('Smile and take your best selfie!!!!', frame)

        # Wait for a key press
        key = cv2.waitKey(1)

        # Press 'spacebar' to take a picture
        if key == 32:
            capture_photo = True  # Set the capture_photo flag to True

        # Press 'q' to exit the loop
        if key == ord('q'):
            print('Saliendo del programa')
            break

    # Release the camera
    cam.release()

    # Close OpenCV windows
    cv2.destroyAllWindows()

    return f'images/cam_pictures/selfie_{img_counter-1}.png'