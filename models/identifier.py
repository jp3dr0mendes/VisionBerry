from classifier import Classifier

import cv2 as cv
import numpy as np

import json
import requests

class Identifier(Classifier):
    def __init__(self):
        with open('data.json','r') as data:
            data_img        = json.load(data)
            self.img_params = data_img["img_params"]

        self.eye               = cv.VideoCapture(0)
        self.valid, self.image = self.eye.read()

        if self.valid:
            while self.valid:
                self.eye = cv.VideoCapture(0)
                self.valid, self.image = self.eye.read()
                self.identifier(self.image)

    def identifier(self, image):

        self.image      = image
        self.img_shape  = self.image.shape
        self.img_height = self.img_shape[0]
        self.img_hsv    = cv.cvtColor(self.image, cv.COLOR_BGR2HSV)        
        self.img_bin    = cv.inRange(self.img_hsv, (self.img_params['hmin'], 100, 100), (self.img_params['hmax'], 255, 255))
        self.img_mop    = cv.morphologyEx(self.img_bin, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_ELLIPSE, (10,10))).astype(np.uint8)
        
        # cv.imshow('image', self.img_mop) 
        # cv.waitKey(1)

        image_contours,img_hierarchy = cv.findContours(self.img_mop, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
        img_obj                      = [cnt for cnt in image_contours if cv.contourArea(cnt) >= max([cv.contourArea(c) for c in image_contours])]

        if(len(img_obj)):

            contour  = img_obj[0]
            img_rect = cv.minAreaRect(contour)
            img_box  = cv.boxPoints(img_rect)
            img_box  = np.intp(img_box) 
            
            cv.drawContours(self.image, contour,-1,(0, 255, 0),2,cv.LINE_AA)
            cv.drawContours(self.image,[img_box],0,(0,0,255),2)
            cv.imshow('imagem', self.image)
            cv.waitKey(1)
            # cv.imshow('Object', self.image)

            # calculando a distancia geométrica
            x_img  = img_rect[0][0]
            y_img  = img_rect[0][1]
            dist_h = img_rect[1][0]
            dist_v = img_rect[1][1]
            comp_y = y_img+dist_v/2

            print('Object Detected')

            # print(self.volumn(contour))
            # print(self.classifier(contour))

            data = {"request": self.classifier(contour)}
            response = requests.get('http://192.168.56.1:5000/classifier', json=data)
            print(response.content)                 
            
            #testando se o objeto está centralizado
            # if((comp_y>(self.img_height*(1-0.2)/2)) & (comp_y<(self.img_height*(1+0.2)/2))): 
            #         # print('Object Detected')
            #         # yield self.image, contour
            #     print('Object Detected')
            #     print(self.volumn(contour))

            # cv.imshow('Video', self.image)                
        else:
            # print("No Object")

            data = {"request": None}
            response = requests.get('http://192.168.56.1:5000/classifier', json=data)
            print(response.content)

Identifier()

        # key = cv.waitKey(1)
        # if key == ord("q"):
        #     return
            