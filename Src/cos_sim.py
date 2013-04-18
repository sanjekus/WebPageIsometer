import re
from numpy import zeros,dot
from numpy.linalg import norm
from nltk import PorterStemmer
from nltk import clean_html
import urllib, urllib2
import urlparse
import httplib
import bs4
import lxml
from lxml.html.clean import Cleaner

__all__=['compare']

#import real stop words
#stop_words = ['i', 'in', 'a', 'to', 'the', 'it', 'have', 'haven\'t', 'was', 'but', 'is', 'be', 'from' ]
#stop_words = [w.strip() for w in open('english.stop','r').readlines()]
#print stop_words

splitter=re.compile ( "[a-z\-']+", re.I )
stemmer=PorterStemmer()

"""
split_text
parameters: string
returns: list of tokens    
"""
def split_text(text):
    text = re.compile("[^\w]|_").sub(" ", text)
    word_list = re.findall("\w+", text.lower())    
    return word_list


'''lists the stop words'''
def list_stop_words():
    stopWords = []
    f = open("stop_words.txt", "rb")
    tokens = f.readlines()
    for token in tokens:
        stopWords.extend(split_text(token))
    return stopWords

stop_words = list_stop_words()

#Recursively follow redirects until there isn't a location header
#http://www.zacwitte.com/resolving-http-redirects-in-python        
def getFinalRedirect(url, depth=0):
    if depth > 10:
        raise Exception("Redirected "+depth+" times, giving up.")
        
    try:
        o = urlparse.urlparse(url,allow_fragments=True)
        conn = httplib.HTTPConnection(o.netloc)
        path = o.path
        if o.query:
            path +='?'+o.query
        conn.request("HEAD", path)
        res = conn.getresponse()
        headers = dict(res.getheaders())
        if headers.has_key('location') and headers['location'] != url:
            return getFinalRedirect(headers['location'], depth+1)
        else:
            return url
    except:
        return False  
    
"""
getHttpContent
parameters: any url
returns: string
"""
def getHtmlContent(url):

    try:
        o = urlparse.urlparse(url,allow_fragments=True)    
                
        #open connection
        conn = httplib.HTTPConnection(o.netloc, timeout=10)
        
        path = '' + o.path
        if o.query != '':
            path += '?'+ o.query
        
        conn.request("GET", path)
        res = conn.getresponse()
        data = res.read()
        
        #close connection
        conn.close()
        return data
        
    except:
        return 'ERROR'

"""
   Adds a word the a dictionary for words/count
   first checks for stop words
   the converts word to stemmed version
"""
def add_word(word,d):
    w=word.lower() 
    if w not in stop_words:
        #ws=stemmer.stem(w,0,len(w)-1)
        ws = stemmer.stem(w)
        d.setdefault(ws,0)
        d[ws] += 1

def doc_vec(doc,key_idx):
    v=zeros(len(key_idx))
    for word in splitter.findall(doc):
        keydata=key_idx.get(stemmer.stem(word.lower()))                 
        if keydata:
            v[keydata[0]] = 1    
    return v

# strip all punctuation but - and '
# convert to lower case
# store word/occurance in dict
def compare(doc1,doc2):
    all_words=dict()
    for dat in [doc1,doc2]:
        [add_word(w,all_words) for w in splitter.findall(dat)]

    # build an index of keys so that we know the word positions for the vector
    key_idx=dict() # key-> ( position, count )
    keys=all_words.keys()
    keys.sort()
    #print keys
    for i in range(len(keys)):
        key_idx[keys[i]] = (i,all_words[keys[i]])
    del keys
    del all_words

    v1=doc_vec(doc1,key_idx)
    v2=doc_vec(doc2,key_idx)
    
    return float(dot(v1,v2) / (norm(v1) * norm(v2)))
 
 
if __name__ == '__main__':
    print "Running Test..."
    url1 = 'http://www.amazon.com/Samsung-I8190-Unlocked-Android-Smartphone/dp/B00A29WCA0/ref=pd_sim_cps_6'
    url2 = 'http://www.amazon.com/Samsung-Galaxy-GT-I9300-Factory-Unlocked/dp/B007VCRRNS'
    final_url1 = getFinalRedirect(url1)
    final_url2 = getFinalRedirect(url2)
    html_content1 = getHtmlContent(final_url1)
    html_content2 = getHtmlContent(final_url2)
    cleaned_html_content1 = clean_html(html_content1)
    cleaned_html_content2 = clean_html(html_content2)
    soup1 = bs4.BeautifulSoup(cleaned_html_content1)
    soup2 = bs4.BeautifulSoup(cleaned_html_content2)
    doc1 = soup1.get_text().encode('ascii', 'ignore')
    doc2 = soup2.get_text().encode('ascii', 'ignore')
    
    print "Similarity %s" % compare(doc1,doc2)
