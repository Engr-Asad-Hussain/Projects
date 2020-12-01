import cv2
import numpy as np

def main():
      path = "C:\\Users\\asadh\\OneDrive - Higher Education Commission\\Computer Vision\\Dataset\\"
      image_path = path + "4.1.04.tiff"

      image = cv2.imread(image_path)
      grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

      face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.XML')
      eye_cascade = cv2.CascadeClassifier('haarcascade_eye.XML')
      
      face = face_cascade.detectMultiScale(grayscale, 1.1, 4)
      for (X, Y, Width, Height) in face:
            cv2.rectangle(image, (X,Y), (X+Width, Y+Height), (255,0,0), 3)
            roi_gray = grayscale[Y:Y+Height, X:X+Width]
            roi_color = image[Y:Y+Height, X:X+Width]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (eX, eY, eWidth, eHeight) in eyes:
                  cv2.rectangle(roi_color, (eX,eY), (eX+eWidth, eY+eHeight), (0,255,0), 2)
                  
      cv2.imshow('Face_Eyes Detection', image)
      cv2.waitKey(0)
      cv2.destroyAllWindows()

if __name__=="__main__":
      main()
