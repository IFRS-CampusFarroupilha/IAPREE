class Dataset:

	information = {
		"author":"",
		"yearReleased":"",
		"source":"",
		"description":""
	}

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