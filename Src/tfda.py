import urllib
from lxml import html
from bs4 import BeautifulSoup
from collections import defaultdict

import re
#taglist=['table','a','img','p']
#tagweights={'table':0.25,'a':0.25,'img':0.25,'p':0.25}
class Tfda:
    
    weight=1
    def __init__(self):
        self.urldict={}
        self.taglist=self.makeTaglist("htmltags.txt")
        num=len(self.taglist)
       
        self.tagweights=self.makeTagweights(self.taglist, num)
        return
    def makeTagweights(self,tags,number):
        tweights={}
        for tag in tags:
            #tweights[tag]=float(1/number)
            tweights[tag]=float(0.05)
        return tweights
    def makeTaglist(self,file):
        tlist=[]
        f = open("../Resources/htmltags.txt", "r")
        lines = [line.strip() for line in f]
        for content in lines:
        #content = f.readlines()t
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
        print(dis)
        return
