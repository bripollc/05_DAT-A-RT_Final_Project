import cv2
import os

def capture_images_from_camera(output_directory):
    os.makedirs(output_directory, exist_ok=True)
    existing_images = os.listdir(output_directory)
    img_counter = len(existing_images)

    cam = cv2.VideoCapture(0)

    while True:
        # capture the frame of the camera
        ret, frame = cam.read()

        # verify if the frame is captured
        if not ret:
            print('Error, it has not been possible to take a picture.')
            break

        # show frame in a window
        cv2.imshow('Smile and take your best selfie!!!!', frame)

        # wait for a key to be pressed
        key = cv2.waitKey(1)

        # press 'spacebar' to take a pic
        if key == 32:
            # name of pic
            img_name = f'selfie_{img_counter}.png'
            img_path = os.path.join(output_directory, img_name)

            # save pic
            cv2.imwrite(img_path, frame)
            print(f'Image saved in: {img_path}')

            # counter increase
            img_counter += 1

        # press 'q' to exit the loop
        if key == ord('q'):
            print('Saliendo del programa')
            break

    # close camera
    cam.release()

    # close opencv windows
    cv2.destroyAllWindows()

    return f'images/cam_pictures/selfie_{img_counter-1}.png'