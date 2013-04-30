###### Implementation of Link Similarity for two web pages ######
######################3
import httplib
import urlparse
import bs4

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
parameters: URL
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
    
def getHrefs(htmlText):
    hrefsList = []
    soup = bs4.BeautifulSoup(htmlText)
    for link in soup.find_all('a'):
        hrefsList.append(link.get('href'))
    return hrefsList

def unique(a):
    """ returns the list with duplicate elements removed """
    return list(set(a))

def intersect(a, b):
    """ returns the intersection of two lists """
    return list(set(a) & set(b))

def union(a, b):
    """ returns the union of two lists """
    return list(set(a) | set(b))

def calculateJaccardValue(hrefsList1, hrefsList2):
    hrefsList1 = [x for x in hrefsList1 if x is not None]
    hrefsList2 = [x for x in hrefsList2 if x is not None]
    hrefsList1 = unique(hrefsList1)
    hrefsList2 = unique(hrefsList2)
    intersectionOfHrefs = intersect(hrefsList1, hrefsList2)
    unionOfHrefs = union(hrefsList1, hrefsList2)
    jaccardValue = float(float(len(intersectionOfHrefs))/float(len(unionOfHrefs)))
    return jaccardValue

if __name__ == '__main__':
    
    "Test Case-1"
    url1 = 'http://www.amazon.com/Samsung-Galaxy-GT-I9300-Factory-Unlocked/dp/B007VCRRNS/ref=sr_1_1?s=electronics&ie=UTF8&qid=1366407073&sr=1-1&keywords=samsung+galaxy+s3'
    url2 = 'http://www.amazon.com/Samsung-Galaxy-SA-I9100-Unlocked-support/dp/B005M3518G/ref=sr_1_1?s=electronics&ie=UTF8&qid=1366415544&sr=1-1&keywords=samsung+galaxy+s2'
    "Test Case-2"
    #url1 = 'http://www.csdl.tamu.edu/~furuta/'
    #url2 = 'http://www.csdl.tamu.edu/~furuta/'
    "Test Case-3"
    #url1 = 'http://www.bbc.com/news/'
    #url2 = 'http://www.bbc.co.uk/sport/0/'
    
    final_url1 = getFinalRedirect(url1)
    final_url2 = getFinalRedirect(url2)
    html_content1 = getHtmlContent(final_url1)
    html_content2 = getHtmlContent(final_url2)
    hrefs1 = getHrefs(html_content1)
    hrefs2 = getHrefs(html_content2)
    
    calculatedJaccardValue = calculateJaccardValue(hrefs1, hrefs2)
    print 'Calculated link similarity between url1 and url2 is %f' %calculatedJaccardValue
