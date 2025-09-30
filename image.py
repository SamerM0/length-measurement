import cv2
import numpy as np
class Image():
    counter = 0
    def __init__(self, path):
        self.path = path
        tmp = cv2.imread(path)
        blurred = cv2.GaussianBlur(tmp, (9, 9), 0)
        gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
        threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 73, 12)
        self.__contours,_ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.__contour = max(self.__contours, key=cv2.contourArea)
        self.__img = cv2.drawContours(tmp, [self.__contour], -1, (0, 255, 0), -1)
        self.id = Image.counter
        Image.counter += 1
    def show_object_image(self):
        cv2.imshow(f"img {self.id}",self.__img)
    def show_all_contours(self):
        cv2.drawContours(self.__img, self.__contours, -1, (0, 255, 0), -1)
        cv2.imshow("All Contours", self.__img)

    def get_horizontal_length(self):
        x,y,w,h = cv2.boundingRect(self.__contour)
        return w
    def get_vertical_length(self):
        x,y,w,h = cv2.boundingRect(self.__contour)
        return h