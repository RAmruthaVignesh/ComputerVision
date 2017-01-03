from PIL import Image
from pylab import *


def clamper(img,rangefrom,rangeto):
    ''' This function takes the input of the image path,
    converts it to grayscale image and 
    clamps its intensities between from and to'''

    #Read the image into array after converting to grayscale
    img = array(Image.open(img).convert('L'))
    # Clamping 
    opimg = ((rangeto-rangefrom)/255.0)*img + rangefrom
    #Convert the image array from float to int
    opimg = uint8(opimg)
    #Convert the imagr to array and return it
    opimg=Image.fromarray(opimg)
    return opimg
    

clamper("../CV_sampleImages/IMG_6628.JPG" , 100,200)