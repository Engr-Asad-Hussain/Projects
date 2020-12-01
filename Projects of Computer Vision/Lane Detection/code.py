import cv2
import numpy as np

def main():
      global window_name
      window_name = 'LANE TRACKER'
      path = "C:\\Users\\asadh\\OneDrive - Higher Education Commission\\Computer Vision\\Dataset\\"
      image_path = path + "Road.JPG"

      image = cv2.imread(image_path)
      image = cv2.resize(image, (512, 512))

      height = image.shape[0]
      width = image.shape[1]

      region_of_interest = [
            (150, width),
            (280, 280), (350,290),
            (480, width)
            ]
      
      grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      threshold1 = 250
      threshold2 = 50
      edges = cv2.Canny(grayscale, threshold1, threshold2, apertureSize=3)

      cropped_image = RegionOfInterest(edges,
                          np.array([region_of_interest], np.int32))
      cv2.imshow('A', cropped_image)
        
      Lines = cv2.HoughLinesP(cropped_image,
                              rho = 6,
                              theta = np.pi/60,
                              threshold = 60,
                              lines = np.array([]),
                              minLineLength = 20,
                              maxLineGap = 25)
      
      final_output = draw_lines(image, Lines)
      cv2.imshow(window_name, final_output)
      cv2.waitKey(0)
      cv2.destroyAllWindows()

def RegionOfInterest(image, vertices):
      mask = np.zeros_like(image)
#      channel_count = image.shape[2]
#      match_mask_color = (255,) * channel_count
      match_mask_color = 255
      cv2.fillPoly(mask, vertices, match_mask_color)
      masked_image = cv2.bitwise_and(image, mask)
      return(masked_image)

def draw_lines(image, Lines):
      image_copy = np.copy(image)
      blank_image = np.zeros( (image.shape[0], image.shape[1], image.shape[2]), dtype=np.uint8)
      if Lines is not None:
            for X1,Y1,X2,Y2 in Lines[0]:
                  cv2.line(image_copy, (X1,Y1), (X2,Y2), (0,0,255), 6)

      return(image_copy)

if __name__=="__main__":
      main()
