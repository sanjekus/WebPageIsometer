import httplib
import urlparse
import bs4
from Utility import *

class LinkSimilarity:
    
    def __init__(self):
        self.utility = Utility()
    
    def calculateJaccardValue(self, hrefsList1, hrefsList2):
        hrefsList1 = [x for x in hrefsList1 if x is not None]
        hrefsList2 = [x for x in hrefsList2 if x is not None]
        hrefsList1 = self.utility.unique(hrefsList1)
        hrefsList2 = self.utility.unique(hrefsList2)
        intersectionOfHrefs = self.utility.intersect(hrefsList1, hrefsList2)
        unionOfHrefs = self.utility.union(hrefsList1, hrefsList2)
        jaccardValue = 0.0
        if len(unionOfHrefs) != 0:
            jaccardValue = float(float(len(intersectionOfHrefs))/float(len(unionOfHrefs)))
        return jaccardValue
    
    def main(self, url1, url2):
        final_url1 = self.utility.getFinalRedirect(url1)
        final_url2 = self.utility.getFinalRedirect(url2)
        html_content1 = self.utility.getHtmlContent(final_url1)
        html_content2 = self.utility.getHtmlContent(final_url2)
        hrefs1 = self.utility.getHrefs(html_content1)
        hrefs2 = self.utility.getHrefs(html_content2)
        calculatedJaccardValue = self.calculateJaccardValue(hrefs1, hrefs2)
        return calculatedJaccardValue
        
'''
if __name__ == '__main__':
    
    "Test Case-1"
    url1 = 'http://www.amazon.com/Samsung-Galaxy-GT-I9300-Factory-Unlocked/dp/B007VCRRNS/ref=sr_1_1?s=electronics&ie=UTF8&qid=1366407073&sr=1-1&keywords=samsung+galaxy+s3'
    url2 = 'http://www.amazon.com/Samsung-Galaxy-SA-I9100-Unlocked-support/dp/B005M3518G/ref=sr_1_1?s=electronics&ie=UTF8&qid=1366415544&sr=1-1&keywords=samsung+galaxy+s2'
    linkSim = LinkSimilarity()
    utility = Utility()
    calculatedJaccardValue = linkSim.main(url1, url2, utility)
    print 'Calculated link similarity between url1 and url2 is %f' %calculatedJaccardValue
'''
