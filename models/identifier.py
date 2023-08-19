import cv2 as cv
import numpy as np

class Identifier:
    def __init__(self, image):
        self.img_params = {
            'hmin': 23,
            'hmax': 39,
            'smax': 0.50,
            'vmax' : 0.57
        }
