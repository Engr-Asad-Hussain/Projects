import cv2
import numpy as np

def main():
      face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.XML')

      cap = cv2.VideoCapture(0)

      while(cap.isOpened()):
            ret, frame = cap.read()
            grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face = face_cascade.detectMultiScale(grayscale, 1.1, 4)

            for (X, Y, Width, Height) in face:
                  cv2.rectangle(frame, (X,Y), (X+Width, Y+Height), (255,0,0), 3)

            cv2.imshow('Face Detection', frame)

            if cv2.waitKey(1) == ord(' '):
                  break

      cap.release()      
      cv2.destroyAllWindows()

if __name__=="__main__":
      main()
