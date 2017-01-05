from PIL import Image
from numpy import *

def pca(img):
    img = array(Image.open(img))

    #get dimensions
    num_data,dim = img.shape

    #calculate mean for each dimension
    shivsai.bal@itcinfotech.com