
import cv2
from tkinter import*


def Cam_Feed():
    """
    This function takes feed from the front facing camera and displays it in
    the screen, it takes in keyboard input; 'q' for quit (saves the image if 
    image is frozen), 's' to freeze the current frame, and 'r' to unfreeze the
    frame to retake picture.

    Return:
        gives back a True or false depending if the image was captured or not 
    """
    #creates an instance of the camera
    cap = cv2.VideoCapture(0)
    while(True):

        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('frame',frame)

        #if user presses 'q' quit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #if user presses 's' captures the picture and
        #freezes it on the screen
        elif cv2.waitKey(1) & 0xFF == ord('s'):
            while (True):
                #if user presses 'q' then the frame is saved
                #to a file 
                if cv2.waitKey(1) & 0xFF == ord('w'):
                    cv2.imwrite('tst.jpeg', frame)
                    cap.release()
                    cv2.destroyAllWindows()
                    return True
                #if the user presser 'r' it tries to retake the
                #picture
                elif cv2.waitKey(1) & 0xFF == ord('r'):
                    break
            
        # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return False
