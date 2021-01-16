class Dataset:

	def __init__(self, information):
		self.information = {
			"author":"",
			"yearReleased":"",
			"source":"",
			"description":""
		}
		
	def __requestDataset(self):
		""" Gets the dataset from some source on the internet """
		raise NotImplementedError

	def getDataset(self):
		""" Returns the processed data from the dataset """
		raise NotImplementedError

	def getInformation(self):
		""" Returns the information from the dataset """
		return self.information

	def __str__(self):
		for key, item in self.information.items():
			print(key, " -> ", item)
		print("Dataset: \n", self.getDataset())