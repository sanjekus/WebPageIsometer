import urllib
from lxml import html
from bs4 import BeautifulSoup
from collections import defaultdict
import re
import random

class StructuralSimilarity:
    
    def __init__(self):
        self.urldict={}
        self.taglist=self.makeTaglist("../Resources/htmltags.txt")
        num=len(self.taglist)
        self.tagweights=self.makeTagweights(self.taglist, num)
        return
    
    def makeTagweights(self,tags,number):
        tweights={}
        for tag in tags:
            tweights[tag]=float(0.05)
        return tweights
    
    def makeTaglist(self,file):
        tlist=[]
        f = open("C:\Users\sanjekus\workspace\webiso\Resources\htmltags.txt", "r")
        lines = [line.strip() for line in f]
        for content in lines:
            mySubString=content[content.find("<")+1:content.find(">")]
            tlist.append(mySubString)
        return tlist
    
    def readURL(self,url):
        self.urldict[url]=defaultdict(int)
        pg=urllib.urlopen(url).read()
        soup = BeautifulSoup(pg)
        for tag in self.taglist:
            self.urldict[url][tag]=len(soup.find_all(tag))
        return
    
    def computeDist(self,url1,url2):
        dist=0
        for tag in self.taglist:
            diff=self.urldict[url1][tag]-self.urldict[url2][tag]
            dist+=diff*diff*(self.tagweights[tag])
        return dist
    
    def compareURL(self,url1,url2):
        self.readURL(url1)
        self.readURL(url2)
        dis=self.computeDist(url1, url2)
        return dis
    
    def main(self, url1, url2):
        distance = self.compareURL(url1, url2)
        distance = float(float(distance)/40000.0)
        distance = float(1.0 - distance)
        distance = abs(distance)
        rand = 0.0
        if distance > 1.0:
            rand = random.uniform(0.99, 1.0)
            distance = rand
        return distance

  
if __name__ == '__main__':
    structureSim = StructuralSimilarity()
    url1 = 'http://www.google.com'
    url2 = 'http://www.rahulgandhiachievements.com/'
    distance = structureSim.main(url1, url2)
    
    print distance

    
    
