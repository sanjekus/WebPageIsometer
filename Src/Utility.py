import httplib
import urlparse
import bs4
import re

class Utility:
    
   
    
    """
    split_text
    parameters: string
    returns: list of tokens    
    """
    def split_text(self,text):
        text = re.compile("[^\w]|_").sub(" ", text)
        word_list = re.findall("\w+", text.lower())    
        return word_list
    
    #Recursively follow redirects until there isn't a location header
    #http://www.zacwitte.com/resolving-http-redirects-in-python        
    def getFinalRedirect(self, url, depth=0):
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
    parameters: URL
    returns: string
    """
    def getCategoryOfURL(self,url):
  	pkl_file = open(Constants.urlIndexPickleFileName, 'rb')
		dictOfURLIndex = pickle.load(pkl_file)
	  	pkl_file.close()
	  	return dictOfURLIndex
	   
    def getHtmlContent(self, url):
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
        
    """ gets the list of hrefs """
    def getHrefs(self, htmlText):
        hrefsList = []
        soup = bs4.BeautifulSoup(htmlText)
        for link in soup.find_all('a'):
            hrefsList.append(link.get('href'))
        return hrefsList
        
    """ returns the list with duplicate elements removed """
    def unique(self, a):
        return list(set(a))

    """ returns the intersection of two lists """
    def intersect(self, a, b):
        return list(set(a) & set(b))

    """ returns the union of two lists """
    def union(self, a, b):
        return list(set(a) | set(b))
    
    '''lists the stop words'''
    def list_stop_words(self):
        stopWords = []
        f = open("../Resources/stop_words.txt", "rb")
        tokens = f.readlines()
        for token in tokens:
            stopWords.extend(self.split_text(token))
        return stopWords
