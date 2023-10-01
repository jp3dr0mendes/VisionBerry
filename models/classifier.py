import cv2 as cv
import numpy as np

import math
import json

class Classifier:
    def classifier(self, rect):
        return self.label(self.volumn(rect))

    def pixel2mm(self,rect):
        with open('data.json','r') as data:
            self.params = json.load(data)

        x        = int(np.max(rect[:,:,0])) - int(np.min(rect[:,:,0]))
        y        = int(np.max(rect[:,:,1])) - int(np.min(rect[:,:,1]))
        realRect = np.array([
        (2*self.params["zmax"]*x)/(2*self.params["focus"]+x),
        (2*self.params["zmax"]*y)/(2*self.params["focus"]+y)])
        
        # realRect = np.array([
        # (2*self.params["zmax"]*int(rect[1][0][0]))/(2*self.params["focus"]+int(rect[1][0][0])),
        # (2*self.params["zmax"]*int(rect[1][0][1]))/(2*self.params["focus"]+int(rect[1][0][1]))])

        return realRect
    
    def volumn(self,rect):
        realRect = self.pixel2mm(rect)
        rx = realRect[0]/2
        ry = realRect[1]/2
        
        if(ry>rx):
            vol = (4*math.pi*ry*rx*rx)
            return vol
        else:
            vol = (4*math.pi*rx*ry*rx)
            return vol

    def label(self, volumn):
        if volumn >= self.params["mean"]: return True
        else: return False