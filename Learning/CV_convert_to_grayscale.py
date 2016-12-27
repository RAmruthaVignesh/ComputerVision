from PIL import Image
img = Image.open('../../../Pictures/BarcelonaNIPS2016/Sagradaside.JPG')

def grayscale(img):
    '''This function takes image input andconverts image to grayscale '''
    img_to_gs = img.convert('L')
    return img_to_gs

x = grayscale(img)
#x.show()