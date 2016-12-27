from PIL import Image
import os

def getimlist(path):
    """ Returns a list of filenames for
    all jpg images in a directory. """
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.JPG')]

print getimlist("../PythonLearning/CV_sampleImages/")