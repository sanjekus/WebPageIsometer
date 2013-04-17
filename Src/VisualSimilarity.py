from Screenshot import Screenshot
import os
from os.path import isfile, join
from Constants import Constants
class VisualSimilarity:
	
	def __init__(self):
		return
	
	
	def takeScreenshot(self,urlOfSite,targetFile,s):
		
		pathOfSavedScreenshotFile = join(Constants.SCREENSHOT_PATH,targetFile)
		if not os.path.exists(pathOfSavedScreenshotFile):
			s.capture(urlOfSite,pathOfSavedScreenshotFile)
	
	
	def prepareScreenshots(self):
		s = Screenshot()
		path = Constants.TRAINING_SET_PATH
		listOfFilesHavingURL=  os.listdir(path)
		for entry in listOfFilesHavingURL:
			if isfile(join(path,entry)):
				f = open(join(path,entry))
				lines = f.readlines()
				for line in lines:
					tokens = line.split('|')
					if len(tokens) >= 4:
						urlOfSite = tokens[2]
						targetFilename = tokens[3]
						self.takeScreenshot(urlOfSite, targetFilename,s)
						
						
					
		
			
			
		
		