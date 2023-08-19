import cv2 as cv
import numpy as np

class Classifier:
    def __init__(self):
        pass
    
    def get_contours(self,hmin: int, hmax: int, smax: int, vmax: int):
        if self.cam.webcam.isOpened():
            valid, frame = self.cam.webcam.read()
            camShape=frame.shape
            camHeight=camShape[0]
            while valid:

                valid, frame = self.cam.webcam.read() 

                img_hsv =  cv.cvtColor(frame, cv.COLOR_BGR2HSV)

                img_bin = np.array(((img_hsv[:,:,0]>hmin) & 
                                    (img_hsv[:,:,0]<hmax) & 
                                    (img_hsv[:,:,1]>smax) &
                                    (img_hsv[:,:,2]>vmax)
                                    )*255, dtype=np.uint8)

'''
import numpy as np
import cv2 as cv
from modules.cam import Cam
# import math 

class Identifier(Cam):
    def __init__(self,hmin,hmax,smax,vmax):
        self.cam = Cam()
        self.get_contours(hmin,hmax,smax,vmax)

    def get_contours(self,hmin: int, hmax: int, smax: int, vmax: int):
        if self.cam.webcam.isOpened(): #Confirma funcionamento da Webcam
            #Primeira leitura da Webcam
            valid, frame = self.cam.webcam.read()
            camShape=frame.shape
            camHeight=camShape[0]
            while valid: #Enquanto leitura valida

                #Atualiza a leitura
                #frame contem 3 canais, cada um com a quantidade de linhas e colunas referênte á resolução da camera
                # (480, 620, 3)
                valid, frame = self.cam.webcam.read() 

                # Converte a Imagem para HSV
                img_hsv =  cv.cvtColor(frame, cv.COLOR_BGR2HSV)

                #Binariza a imagem HSV levando em conta as condições de cores:
                img_bin = np.array(((img_hsv[:,:,0]>hmin) & 
                                    (img_hsv[:,:,0]<hmax) & 
                                    (img_hsv[:,:,1]>smax) &
                                    (img_hsv[:,:,2]>vmax)
                                    )*255, dtype=np.uint8)

                #Aplica a transformação morfológica de fechamento para eliminar ruidos
                img_mop = cv.morphologyEx(img_bin, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_ELLIPSE, (10, 10))).astype(np.uint8)


                # cv.imshow('Camera', frame)
                cv.waitKey(1)
                
                contours,hierarchy = cv.findContours(img_mop, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
                # A variável contours contem listas de contornos
                # Cada contorno por sua vez é uma matriz (n,1,2), onde n é o numero de pontos que 
                # definem as bordas do objeto, representados por um vetor de dois valores (x,y)
                
                #Maior objeto detectado
                cntr=[cnt for cnt in contours if cv.contourArea(cnt) >= max([cv.contourArea(c) for c in contours])]
                
                # cv.imshow('Objeto detectado', frame)
                if(len(cntr)):
                    contour=cntr[0]
                    # (center(x, y), (width, height), angle of rotation) = cv2.minAreaRect(points)
                    # https://theailearner.com/tag/cv2-minarearect/
                    rect = cv.minAreaRect(contour)
                    box = cv.boxPoints(rect)
                    box = np.int0(box)

                    cv.drawContours(frame, contours,-1,(0, 255, 0),2,cv.LINE_AA)
                    cv.drawContours(frame,[box],0,(0,0,255),2)
                    cv.imshow('Objetos de prova', frame)

                    # Objeto está centralizado?
                    x = rect[0][0]
                    y = rect[0][1]
                    d_h = rect[1][0]
                    d_v = rect[1][1]
                    cY=y+d_v/2

                    print(rect)

                    if((cY>(camHeight*(1-0.2)/2)) & (cY<(camHeight*(1+0.2)/2))): 
                        print("Objeto detectado!")
                        # self.real_scale(frame,contour)
                        # cv.waitKey(1)
                        # return frame,contour                       
        else:
            print("Erro de conexão da webcam")
            return 0
'''