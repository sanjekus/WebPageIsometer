class Constants:
	'''General'''
	TRAINING_SET_PATH="../Resources/TrainingSet"
	SCREENSHOT_PATH= "../Resources/Screenshots"
	
	
	
	'''Structural Similarity'''
	listOfTags=["TABLE","DEFINITION_LIST","ORDERED_LIST","UNORDERED_LIST","BREAKS"]
	
	weightsOfTag=	{
		"UNORDERED_LIST":{"LENGTH_OF_STRING":0.2 ,"LEF_Of_String":0.4,"SUM" : 0.2,"AVG":0.2},
		"ORDERED_LIST" :{"LENGTH_OF_STRING":0.2 ,"LEF_Of_String":0.4,"SUM" : 0.2,"AVG":0.2},
		"DEFINITION_LIST":{"LENGTH_OF_STRING":0.2 ,"LEF_Of_String":0.4,"SUM" : 0.2,"AVG":0.2}
	}
	
	
	
	'''Total Similarity Weights'''
	simWeightDict={"SPORTS":{"CONTENT":0.3,"VISUAL":0.5,"STRUCTURAL":0.2},
				"ECOMMERCE_PHONE":{"CONTENT":0.3,"VISUAL":0.5,"STRUCTURAL":0.2}}			
	
	
	def __init__(self):
		return

