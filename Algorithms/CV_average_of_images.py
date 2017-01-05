import sys
sys.path.append('../Learning/')
sys.path.append('../../PythonLearning/')
from PIL import Image
from pylab import *
import numpy as np
import os
from CV_list_of_files_in_folder import *

imlist =  getimlist("../CV_sampleImages/")

def compute_average(imlist):
    # open first image and make into array of type float
    averageimg = array(Image.open(imlist[0]) ,'f')
    for imname in imlist[1:]:
        try:
            averageimg += array(Image.open(imname))
        except:
            print imname + '...skipped'
        averageimg = averageimg/len(imlist)
        return uint8(averageimg)


avgopimg = compute_average(imlist)
avgopimg = Image.fromarray(avgopimg)
avgopimg.show()