from PIL import Image
import os

def resize(img,x,y):
    '''This function takes the input of the image to be resized and desired resolution
    and resizes the image accordingly'''
    outfile = os.path.splitext(img)[0]+'resized'
    img = Image.open(img)
    opimg = img.resize((x,y))
    opimg.save(outfile,'JPEG')
    Image.open(outfile).show()

def rotateimg(img,angle):
    '''This function takes the input of the image to be rotated and desired angle
    and rotates the image accordingly'''
    outfile = os.path.splitext(img)[0]+'rotated'
    img=Image.open(img)
    opimg = img.rotate(angle)
    opimg.save(outfile,'JPEG')
    Image.open(outfile).show()

resize("../PythonLearning/CV_sampleImages/IMG_6625.JPG",128,128)
rotateimg("../PythonLearning/CV_sampleImages/IMG_6625.JPG",45)