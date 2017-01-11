from PIL import Image
import os

def cropimage(img,a,b,c,d):
    '''Takes 5 inputs-
    img-image to be cropped
    a,b,c,d - coordinates left,upper,right,lower
    and crops the defined region
    '''
    outfile = os.path.splitext(img)[0]+'croppedregion'
    box = (a,b,c,d)
    img= Image.open(img)
    region = img.crop(box)
    region.save(outfile,'JPEG')
    Image.open(outfile).show()

def pasteimage(img,baseregion,a,b,c,d):
    '''Takes 6 inputs-
    img-image to be pasted
    baseregion-the area on which the image is pasted
    a,b,c,d - coordinates left,upper,right,lower
    and pastes img on baseregion
    '''
    outfile = os.path.splitext(baseregion)[0]+'pasted'
    img = Image.open(img)
    baseregion = Image.open(baseregion)   
    baseregion.show()
    box=(a,b,c,d)
    baseregion.paste(img,box)
    baseregion.save(outfile,'JPEG')
    Image.open(outfile).show()


cropimage("../PythonLearning/CV_sampleImages/IMG_6625.JPG",400,500,600,700)
pasteimage("../PythonLearning/CV_sampleImages/IMG_6625croppedregion","../PythonLearning/CV_sampleImages/IMG_6625.JPG",1000,1100,1200,1300)



