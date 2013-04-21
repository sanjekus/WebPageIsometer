from StructuralSimilarity import *
from ContentSimilarity import *
#from VisualSimilarity import *
from LinkSimilarity import *
import numpy as np

class WebPageSimilarity:
    
    def __init__(self):
        self.structuralSimilarity = StructuralSimilarity()
        self.contentSimilarity = ContentSimilarity()
        #self.visualSimilarity = VisualSimilarity()
        self.linkSimilarity = LinkSimilarity()
        
    def calculate_similarity(self, url1, url2):
        similarity_dict = {}
        similarity_dict['content_similarity'] = self.contentSimilarity.main(url1, url2)
        similarity_dict['link_similarity'] = self.linkSimilarity.main(url1, url2)
        #similarity_dict['visual_similarity'] = self.visualSimilarity(url1, url2)
        similarity_dict['structural_similarity'] = self.structuralSimilarity.main(url1, url2)
        return similarity_dict
    
    def calculate_weights(self, listOfCalculatedSimilarities, listOfActualSimilarities):
        a = np.array(listOfCalculatedSimilarities)
        b = np.array(listOfActualSimilarities)
        result = np.linalg.lstsq(a, b)
        return result
            
if __name__ == '__main__':
    webPageSimilarity = WebPageSimilarity()
    #file = open('../Resources/results.txt', 'wb')
    f = open('../Resources/TrainingSet/Education.txtResult.txt', 'rb')
    urls = f.readlines()
    f.close()
    globalListOfCalculatedWeights = []
    listOfCalculatedSimilarities = []
    listOfActualSimilarities = [0.8, 0.5, 0.3]
    count = 0
    for i in range(len(urls)):
        j = i
        while j < (len(urls)-1):
            j += 1
            url1 = urls[i].strip()
            url2 = urls[j].strip()
            similarity_dict = webPageSimilarity.calculate_similarity(url1, url2)
            print urls[i]
            print urls[j]
            temp_listOfCalculatedSimilarities = []
            for key, value in similarity_dict.items():
                print key, value
                temp_listOfCalculatedSimilarities.append(value)
            listOfCalculatedSimilarities.append(temp_listOfCalculatedSimilarities)
            print '#########################################'
            count += 1
            if count == len(listOfActualSimilarities):
                result = webPageSimilarity.calculate_weights(listOfCalculatedSimilarities, listOfActualSimilarities)
                list_result = list(result)
                print 'Calculated weights:', list_result
                globalListOfCalculatedWeights.append(result)
                listOfCalculatedSimilarities = []
                count = 0
                print '###########################################'
            
    print 'Estimated weights after training is calculated as:'
    final_estimated_weights = []
    for i in range(len(listOfActualSimilarities)):
        final_estimated_weights[i] = 0.0
    for list in globalListOfCalculatedWeights:
        for index in range(len(list)):
            final_estimated_weights[index] += list[index]
            
    length = len(globalListOfCalculatedWeights)
    final_estimated_weights = [x/length for x in final_estimated_weights]
    
    print 
    print 'finally estimated weights:'
    for elem in final_estimated_weights:
        print elem
        
                
                
                
    
    
    
    
        
        
        
    
    




