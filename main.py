import cv2
import numpy as np


from image import Image
def main():

    imgS1 = "./img1.jpg" #16 cm
    imgS2 = "./img2.jpg" #12 cm
    imgS3 = "./img3.jpg" #? cm

    img1 = Image(imgS1)
    img2 = Image(imgS2)
    cv2.imshow("img1", img1.get_image_object())
    cv2.imshow("img2", img2.get_image_object())

    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()