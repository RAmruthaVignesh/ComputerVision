from PIL import Image
from pylab import *
from CV_preprocessing import *

#Read the image into array and plot it
img = plotimg_from_array("../CV_sampleImages/IMG_6625.JPG")
print "please click 3 points"

#Get user input coordinates
x=ginput(3)
plot(x)
print "You clicked :" , x
show()

