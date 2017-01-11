from PIL import Image
from pylab import *
from CV_preprocessing import *

#open the image
img = openimg("../PythonLearning/CV_sampleImages/IMG_6628.JPG")
#Convert image to grayscale
img = grayscale(img)
#read image to array
img =getarray_from_img(img)

# create a new figure
figure()
#dont use colors
gray()

# show contours with origin upper left corner
contour(img, origin='image')
axis('equal')
axis('off')
show()

