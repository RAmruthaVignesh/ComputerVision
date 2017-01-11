from PIL import Image
from pylab import *
import os

def openimg(path):
    '''This function opens the image from the input path for further processing'''
    opimg = Image.open(path)
    return opimg

def getarray_from_img(img):
    '''This function reads image and converts it to array'''
    img=openimg(img)
    getarray = array(img)
    return getarray

def plotimg_from_array(matimg):
    '''This function plots the matrix'''
    #opimg=array(Image.open(img))
    opimg = imshow(arrayimg)
    return opimg

def plot_marker_in_img(img,x,y,plottitle,marker='go-'):
    '''This function takes the input of 
    img - plotted image and list of x and y coordinates.
    Plots the x,y in the image with red star markers.
    markers - Default marker is green circle , desired marker can be inputted
    '''
    if len(x)==len(y):
        plot(x,y,marker)
        # line plot connecting the first three points
        opimg = plot(x[:3],y[:3])
        # add title and show the plot
        title(plottitle)
        #show()
        return opimg
    else:
        print "Invalid coordinates"

def removeaxis():
    '''This function removes axis in the plot to create prettier plot'''
    axis('off')



arrayimg = getarray_from_img("../CV_sampleImages/IMG_6627.JPG")
opimg1= plotimg_from_array(arrayimg)
opimg2 =plot_marker_in_img(opimg1,[1000,2000,1500,2000],[200,500,200,400],'Plotting: Points of interest')
removeaxis()
#show()



