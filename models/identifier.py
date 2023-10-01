from classifier import Classifier

import cv2 as cv
import numpy as np
import json

class TesteIdentifier(Classifier):
    def __init__(self):
        with open('data.json','r') as data:
            data_img        = json.load(data)
            self.img_params = data_img["img_params"]

        self.eye = cv.VideoCapture(0)
        self.valid, self.image = self.eye.read()
        if self.valid:
            count=1
            while self.valid:
                print(count)
                self.eye = cv.VideoCapture(0)
                self.valid, self.image = self.eye.read()
                self.identifier(self.image)
                count += 1
    def identifier(self, image):
        print('init')

        # self.valid, self.image     = self.eye.read()
        # self.valid, self.image = eye.read()

        # self.valid     = True
        # self.image = cv.imread('8-fruto-apropriado-0.23x0.265.jpg', cv.COLOR_BGR2HSV)
        self.image = image
        self.img_shape             = self.image.shape
        self.img_height            = self.img_shape[0]
            # self.valid, self.image = self.eye.read()
        self.img_hsv           = cv.cvtColor(self.image, cv.COLOR_BGR2HSV)
        # self.img_bin           =  np.array(((self.img_hsv[:,:,0] > self.img_params['hmin']) & 
        #                                     (self.img_hsv[:,:,0] < self.img_params['hmax']) & 
        #                                     (self.img_hsv[:,:,1] > self.img_params['smax']) &
        #                                     (self.img_hsv[:,:,2] > self.img_params['vmax'])), dtype=np.uint8)
        
        # Funcionou!!!
        self.img_bin = cv.inRange(self.img_hsv, (self.img_params['hmin'], 100, 100), (self.img_params['hmax'], 255, 255))

        # inf_lim = np.array([20, 100, 100])
        # sup_lim = np.array([105, 255,255])

        # mascara = cv.inRange(self.img_hsv, inf_lim, sup_lim)
        # self.img_bin = cv.bitwise_and(self.image, self.image, mask=mascara)
        # cv.imshow('image', self.img_bin) 
        # cv.waitKey(1)  

        self.img_mop           = cv.morphologyEx(self.img_bin, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_ELLIPSE, (10,10))).astype(np.uint8)
        cv.imshow('image', self.img_mop) 
        cv.waitKey(0)

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
            # cv.imshow('Object', self.image)

            # calculando a distancia geométrica
            x_img  = img_rect[0][0]
            y_img  = img_rect[0][1]
            dist_h = img_rect[1][0]
            dist_v = img_rect[1][1]
            comp_y = y_img+dist_v/2

            print('Object Detected')
            print(self.volumn(contour))
                
            #testando se o objeto está centralizado
            # if((comp_y>(self.img_height*(1-0.2)/2)) & (comp_y<(self.img_height*(1+0.2)/2))): 
            #         # print('Object Detected')
            #         # yield self.image, contour
            #     print('Object Detected')
            #     print(self.volumn(contour))

            # cv.imshow('Video', self.image)                
        else:
            print("No Object")
        key = cv.waitKey(1)
        if key == ord("q"):
            return
            

TesteIdentifier()

class Identifier:
    def __init__(self):
        with open('data.json','r') as data:
            data_img        = json.load(data)
            self.img_params = data_img["img_params"]
            for i in self.img_params:
                print(i)

    def start(self):
        try:
            self.eye    = cv.VideoCapture(0)
            self.identifier()
        except:
            print("Identifier Error")

    def identifier(self):
        
        self.valid, self.image     = self.eye.read()
        self.img_shape             = self.image.shape
        self.img_height            = self.img_shape0[0]

        while self.valid:
            
            self.valid, self.image = self.eye.read()
            self.img_hsv           = cv.cvtColor(self.image, cv.COLOR_BGR2HSV)
            self.img_bin           =  np.array(((self.img_hsv[:,:,0] > self.img_params['hmin']) & 
                                            (self.img_hsv[:,:,0] < self.img_params['hmax']) & 
                                            (self.img_hsv[:,:,1] > self.img_params['smax']) &
                                            (self.img_hsv[:,:,2] > self.img_params['vmax']))*255, dtype=np.uint8)
            
            self.img_mop           = cv.morphologyEx(self.img_bin, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_ELLIPSE, (10,10))).astype(np.uint8)

            cv.imshow('Video', self.image)
            cv.waitKey(1)
            cv.destroyAllWindows()

            image_contours,img_hierarchy = cv.findContours(self.img_mop, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
            img_obj                      = [cnt for cnt in image_contours if cv.contourArea(cnt) >= max([cv.contourArea(c) for c in image_contours])]

            if(len(img_obj)):

                contour  = img_obj[0]
                img_rect = cv.minAreaRect(contour)
                img_box  = cv.boxPoints(img_rect)
                img_box  = np.int0(img_box) 
            
                cv.drawContours(self.image, contour,-1,(0, 255, 0),2,cv.LINE_AA)
                cv.drawContours(self.image,[img_box],0,(0,0,255),2)
                cv.imshow('Object', self.image)

                # calculando a distancia geométrica
                x_img  = img_rect[0][0]
                y_img  = img_rect[0][1]
                dist_h = img_rect[1][0]
                dist_v = img_rect[1][1]
                comp_y = y_img+dist_v/2
                
                #testando se o objeto está centralizado
                if((comp_y>(self.img_height*(1-0.2)/2)) & (comp_y<(self.img_height*(1+0.2)/2))): 
                    # print('Object Detected')
                    yield self.image, contour
                
                key = cv.waitKey(1)
                if key == ord("q"):
                    break
            
            cv.destroyAllWindows()

# def start(self):
        # try:
        #     self.eye    = cv.VideoCapture(0)
        #     self.identifier()
        # except:
        #     print("Identifier Error")