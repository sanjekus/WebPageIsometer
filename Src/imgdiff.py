
from PIL import ImageChops
import math, operator
from Image import *

"Calculate the root-mean-square difference between two images"
def rmsdiff(im1, im2):
    diff = ImageChops.difference(im1, im2)
    h = diff.histogram()
    sq = (value*(idx**2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares/float(im1.size[0] * im1.size[1]))
    return rms

if __name__ == '__main__':
    im1 = open('website3.png')
    im2 = open('website4.png')
    im3 = open('website.png')
    im5 = open('website5.png')
    rms_sim = rmsdiff(im1, im2)
    rms_dif = rmsdiff(im1, im3)
    rms_dif1 = rmsdiff(im1, im5)
    print rms_sim, rms_dif, rms_dif1
    