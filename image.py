import cv2
import numpy as np
class Image():
    counter = 0 # used to create different window names
    def __init__(self, path):
        self.path = path
        tmp = cv2.imread(path)
        blurred = cv2.GaussianBlur(tmp, (9, 9), 0) # reduce noise
        gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY) #change from bgr to gray
        threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 73, 12) # change to a binary image
        self.__contours,_ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # find different contours
        self.__contour = max(self.__contours, key=cv2.contourArea) # find biggest contour (most likely the main object)
        self.__img = cv2.drawContours(tmp, [self.__contour], -1, (0, 255, 0), -1) # save image with contour
        self.id = Image.counter
        Image.counter += 1 
        
    def show_object_image(self):
        cv2.imshow(f"object {self.id}",self.__img) # show object contour only

    def show_all_contours(self):
        tmp = cv2.drawContours(self.__img.copy(), self.__contours, -1, (0, 255, 0), -1)
        cv2.imshow(f"All Contours {self.id}",tmp) # show all contours

    def get_horizontal_length(self):# get width
        x,y,w,h = cv2.boundingRect(self.__contour) 
        return w
    
    def get_vertical_length(self):# get height
        x,y,w,h = cv2.boundingRect(self.__contour)
        return h