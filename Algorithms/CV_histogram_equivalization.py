import sys
sys.path.append('../Learning/')
sys.path.append('../../PythonLearning/')
from PIL import Image
from pylab import *
import numpy as np
from CV_preprocessing import *

def histeq(img,bins=256,dispimg=False):

    #Open the image
    img = array(Image.open(img).convert('L'))
    
    #Flatten the 2D image to 1D and then create a histogram,and 2nd arguement represents number of bins used
    histimg,bins = np.histogram(img.flatten(),bins,normed=True)
    cdf = histimg.cumsum() # cumulative distribution function
    cdf = 255 * cdf

    # use linear interpolation of cdf to find new pixel values - The values of img.flatten is replaced with cdf according to bins 
    im2 = interp(img.flatten(),bins[:-1],cdf)
    #The flattened im2 is reshaped
    im2 = im2.reshape(img.shape)

    #Displays the before and after images
    if dispimg==True:
        fig=before_and_after(img,"Before Histogram equivalization",im2,"After Histogram equivalization")
        show()
    #Image is retrieved from array
    im2 = Image.fromarray(im2)
    return im2,cdf


imghisteq,cdf = histeq("../CV_sampleImages/IMG_6635.JPG",256,True)
