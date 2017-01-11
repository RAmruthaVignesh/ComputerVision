from PIL import Image
from pylab import *
from numpy import *

def pca(img):
    img = array(Image.open(img).convert('L'))

    #get dimensions
    num_data,dim = img.shape

    #calculate mean for each dimension
    mean_each_dim = img.mean(axis=0) #axis =0 calculates the column mean
    #calculate the variance - distance from the mean
    SD_img = img - mean_each_dim 

    if dim > num_data:
        #calculates the covariance matrix as AA' instead of A'A by compact trick
        covmat = dot(SD_img,SD_img.T) 
        #calculates the eigen vector and eigen values of the covariance matrix
        e,EV = linalg.eigh(covmat) 
        tmp = dot(SD_img.T,EV).T # This is the compact trick
        V=tmp[::-1] #Reversing to arrange the Eigen vectos in the descending order
        # the eigen values,e are the variances . sqrt(e) gives the S.D which are the singular values
        s=sqrt(e)[::-1]
        #Dividing by S.D gives the normalization
        for i in range(V.shape[1]):
            V[:,i] /= s 
    else:
        # PCA - SVD used
        U,s,V = linalg.svd(img)
        V =V[:,num_data]
    #Return the Eigen vectos , singular values,mean
    return V,s,mean_each_dim

V,s,immean = pca("../CV_sampleImages/IMG_6628.JPG")
img = array(Image.open("../CV_sampleImages/IMG_6628.JPG").convert('L'))
m,n = img.shape[0:2]
figure()
gray()
imshow(V)
show()
