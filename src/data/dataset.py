class Dataset:

	information = {
		"author":"",
		"yearReleased":"",
		"source":"",
		"description":""
	}

	@staticmethod
	def getBestOptimizer():
		""" Gets the best of the AI if you use this dataset """
		raise NotImplementedError

	@staticmethod
	def getBestLoss():
		""" Gets the start of the AI if you use this dataset """
		raise NotImplementedError

	@staticmethod
	def getStart():
		""" Gets the start of the AI """
		raise NotImplementedError

	@staticmethod
	def getEnd():
		""" Gets the end of the AI """
		raise NotImplementedError

	@staticmethod
	def __requestDataset():
		""" Gets the dataset from some source on the internet """
		raise NotImplementedError

	@staticmethod
	def getDataset():
		""" Returns the processed data from the dataset """
		raise NotImplementedError

	@staticmethod
	def getInformation():
		""" Returns the information from the dataset """
		return Dataset.information