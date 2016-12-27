from PIL import Image
from pylab import *
from CV_preprocessing import *

#Open the image
img = openimg("../PythonLearning/CV_sampleImages/IMG_6635.JPG")
#Convert the image to grayscale
img=grayscale(img)
#Read image into array
img=getarray_from_img(img)

#create a new figure
figure()
#Flatten the 2D image to 1D and then create a histogram,and 2nd arguement represents number of bins used
hist(img.flatten(),128)
show()