from PIL import Image
import os

def jpg_to_png(folder):
    for infile in os.listdir(folder):
        print "infile:" , infile
        outfile = os.path.splitext(infile)[0] + '.png'
        print "outfile:" , outfile
        if infile !=outfile:
            try:
                Image.open("../PythonLearning/CV_sampleImages/"+infile).save("../PythonLearning/CV_sampleImages/"+outfile)
            except IOError:
                print "cannot convert",infile



jpg_to_png("../PythonLearning/CV_sampleImages/")