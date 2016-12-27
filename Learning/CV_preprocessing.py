from PIL import Image
from pylab import *
import os

def openimg(path):
    '''This function opens the image from the input path for further processing'''
    opimg = Image.open(path)
    return opimg

def getarray_from_img(img):
    '''This function reads image and converts it to array'''
    #img=openimg(img)
    getarray = array(img)
    return getarray

def grayscale(img):
    '''This function takes image input andconverts image to grayscale '''
    img_to_gs = img.convert('L')
    return img_to_gs

def plotimg_from_array(img):
    '''This function plots the matrix'''
    opimg=array(Image.open(img))
    opimg = imshow(opimg)
    return opimg