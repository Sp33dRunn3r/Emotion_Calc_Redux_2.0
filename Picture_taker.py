#(Function used for specific machine learning purposes)

import cv2

def take_selfie():
    Confirm_take_selfie = input('''
    Would you like to take a selfie?

    Type "Yes" to take picture.
    Type "Quit" to eConfirm_take_selfieit the application.

    ''')
    if Confirm_take_selfie.lower() == 'yes':
        cam = cv2.VideoCapture(0)

        cv2.namedWindow("test")

        img_counter = 0

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                # ESC pressed
                print("\"Q\" selected Closing Program")
                break
            elif key == ord('s'):
                # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} Saving. Picture successfully taken!".format(img_name))
                img_counter += 1

        cam.release()


        exit()
    elif Confirm_take_selfie.lower() == 'quit':
        print('Have a nice day! (Closing Program)')
        exit()
    return 'Process Completed!'
