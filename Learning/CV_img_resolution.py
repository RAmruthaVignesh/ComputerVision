from PIL import Image
from pylab import *
from CV_preprocessing import *
import os

def resolution(img):
    '''This function takes the input of path of the image file and gives the
    output of resolution of the image'''
    img = array(Image.open(img))
    img_resolution = img.shape
    return img_resolution

print resolution("../CV_sampleImages/IMG_6625.JPG")
