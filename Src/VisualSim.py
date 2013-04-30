from PIL import ImageChops
from VisualSimilarity import *
import math, operator
import random
import sys
#from Image import *
from PIL import Image
import os


class VisualSim:
    
    """Calculate the root-mean-square difference between two images"
    def rmsdiff(self, im1, im2):
        #diff = ImageChops.difference(im1, im2)
        #h = diff.histogram()
        sq = (value*(idx**2) for idx, value in enumerate(h))
        sum_of_squares = sum(sq)
        rms = math.sqrt(sum_of_squares/float(im1.size[0] * im1.size[1]))
        return rms
    
  """   

    def main(self, im1, im2):
        im1 = Image.open(im1)
        im2 = Image.open(im2)
       
        h1 = im1.histogram()
        h2 = im2.histogram()
        rms = math.sqrt(reduce(operator.add,
                           map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
        rms = float(float(rms)/float(100000.0))
        a = float(1.0 - rms)
    	a= abs(a)
        if a > 1.0:
            rms_temp = random.uniform(0.99, 1.0)
            a = rms_temp
            rms = a
  
        return rms
     
    def returnSim(self,url1,url2):
    	out1='C:\Users\sanjekus\Desktop\url1.png'
    	out2='C:\Users\sanjekus\Desktop\url2.png'
        vs1 = VisualSimilarity()
    	vs1.capture(url1,out1)
        vs2 = VisualSimilarity()
        vs2.capture(url2,out2)
    	#VisualSimilarity().capture(url2,out2)
    	rms=self.main(out1,out2) 
        '''
        filelist = [ f for f in os.listdir("C:\Users\sanjekus\workspace\webiso\Sources") if f.endswith(".png")]
        for f in filelist:
            os.remove("C:\Users\sanjekus\workspace\webiso\Source\%s" %f)
        '''
        return rms
	
    

if __name__ == '__main__':
    vizSim = VisualSim()
    url1 = 'http://www.google.com'
    url2 = 'http://www.yahoo.com'
    rms = vizSim.returnSim(url1, url2)
    print rms
    
    
    #p = "C:\Users\sanjekus\workspace\webiso\Resources\Screenshots\e_books"
    #path=os.path.join(p)
    #vizSim.findNremove(path,".png")
    
    #filelist = [ f for f in os.listdir("C:\Users\sanjekus\workspace\webiso\Resources\Screenshots\e_books") if f.endswith(".png") ]
    #for f in filelist:
    #os.remove("C:\Users\sanjekus\workspace\webiso\Resources\Screenshots\e_books\%s" %f)
    #os.remove('C:\Users\sanjekus\workspace\webiso\Resources\Screenshots\e_books\0.png')
    
    
    
    '''
    im1 = open('website3.png')
    im2 = open('website4.png')
    im3 = open('website.png')
    im5 = open('website5.png')
    rms_sim = rmsdiff(im1, im2)
    rms_dif = rmsdiff(im1, im3)
    rms_dif1 = rmsdiff(im1, im5)
    print rms_sim, rms_dif, rms_dif1
    '''
