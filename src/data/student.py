from utils.consts import TRAIN_PORCENTAGE, PROJECT_ROOT
from data.dataset import Dataset
import pandas as pd

class studentDataset(Dataset):

	def __init__(self):
		super().__init__({
			"author":"Me",
			"yearReleased":"2020",
			"source":"Vozes da minha cabeça",
			"description":"teste"
		})

		self.__requestDataset()

	def getDataset(self):

		xTrain = self.dataset
		
		xTest = xTrain[int(len(xTrain)*TRAIN_PORCENTAGE)+1:len(xTrain)]
		xTrain = xTrain[0:int(len(xTrain)*TRAIN_PORCENTAGE)]

		yTrain = xTrain.pop("final_result")
		yTest = xTest.pop("final_result")

		xTrain = pd.get_dummies(xTrain)
		yTrain = pd.get_dummies(yTrain)

		xTest = pd.get_dummies(xTest)
		yTest = pd.get_dummies(yTest)	

		return (xTrain, yTrain, xTest, yTest)

	def __requestDataset(self):
		self.dataset = pd.read_csv(PROJECT_ROOT+"/datasets/studentInfo.csv")