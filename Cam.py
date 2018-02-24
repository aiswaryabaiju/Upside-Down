import numpy as np
import cv2


def CamFeed():
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
            
        # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def main():
    CamFeed()

if __name__ == "__main__":
    main()