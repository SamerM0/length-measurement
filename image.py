import cv2
import numpy as np
class Image():
    def __init__(self, path):
        self.path = path
        tmp = cv2.imread(path)
        blurred = cv2.GaussianBlur(tmp, (9, 9), 0)
        gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
        threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 6)
        contours,_ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contour = max(contours, key=cv2.contourArea)
        self.__img = cv2.drawContours(tmp, [contour], -1, (0, 255, 0), -1)
    def get_image_object(self):
        return self.__img