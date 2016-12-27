from PIL import Image
import os

def thumbnail(imgip):
    '''This function takes the input of an image
    Converts it to thumbnail of size (128,128)
    and saves it'''
    outfile = os.path.splitext(imgip)[0]+'thumbnail'
    imgip = Image.open(imgip)
    #imgip.show()
    imgip.thumbnail((128,128))
    imgip.save(outfile,"JPEG")
    Image.open(outfile).show()

thumbnail("../PythonLearning/CV_sampleImages/IMG_6625.JPG")