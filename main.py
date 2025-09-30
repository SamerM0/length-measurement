import cv2
import numpy as np


from image import Image
from length_calculator import LengthCalculator
def main():
    imgS4 = "./img4.jpg" #12 cm width
    imgS5 = "./img5.jpg" #10.7 cm width

    img1 = Image(imgS4)
    img2 = Image(imgS5)
    width = LengthCalculator.calculate_length(img1.get_horizontal_length(), 12, img2.get_horizontal_length())
    print(f"width: {width} cm")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()