from PIL import Image
from pylab import *
from numpy import *
import pickle
import os

def getimlist(path):
    """ Returns a list of filenames for
    all jpg images in a directory. """
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.pgm')]

def pca(flat_img_array):
    ''' Gets the input of a matrix with the flattened arrays in rows. 
    Returns the projection matrix,variance and mean'''

    #get dimensions
    num_data,dim = flat_img_array.shape

    #calculate mean for each dimension
    mean_each_dim = flat_img_array.mean(axis=0) #axis =0 calculates the column mean
    #calculate the variance - distance from the mean
    SD_img = flat_img_array - mean_each_dim 

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

#list of all images in a folder
imlist = getimlist("../CV_sampleImages/s1")
#Read 1 image to get the size
im = array(Image.open(imlist[0]))
m,n = im.shape[0:2]

if os.path.isfile('pca_values.pkl') == False : #If the pickle file doesn't exist

    #total number of images in the list
    imnbr = len(imlist)

    #create a matrix to store all flattened images
    immatrix = array([array(Image.open(im)).flatten() for im in imlist],'f')
    #Apply PCA
    V,s,immean = pca(immatrix)

    #Picking the file
    with open('pca_values.pkl','wb') as f:
        pickle.dump(immean,f)
        pickle.dump(V,f)

#open the pickle file and load
with open('pca_values.pkl','rb') as f:
    immean = pickle.load(f)
    V=pickle.load(f)


figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(V[i].reshape(m,n))
show()




