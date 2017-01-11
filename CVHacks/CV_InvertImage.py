from PIL import Image
from pylab import *
import os
from CV_preprocessing import *

def invert(img):
    '''This function takes in the path of the image file and 
    inverts the graylevels of the image and returns it'''
    #Read the image into array after converting to grayscale
    img = array(Image.open(img).convert('L'))
    #Perform inversion of graylevels
    opimg = 255-img
    #convert the array to image and return it
    return Image.fromarray(opimg)

invert("../CV_sampleImages/IMG_6627.JPG").show()