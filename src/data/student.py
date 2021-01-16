from utils.consts import TRAIN_PORCENTAGE, PROJECT_ROOT
from data.dataset import Dataset
import pandas as pd

class studentDataset(Dataset):

	information = {
		"title": "Open University Learning Analytics Dataset",
		"author": "The Open University",
		"yearReleased":"2015",
		"source":"https://analyse.kmi.open.ac.uk/open_dataset",
		"description":"Contains data about courses, students and their interactions with Virtual Learning Environment (VLE) for seven selected courses (called modules)"
	}

	@staticmethod
	def getDataset():

		xTrain = studentDataset.__requestDataset()
		
		xTest = xTrain[int(len(xTrain)*TRAIN_PORCENTAGE)+1:len(xTrain)]
		xTrain = xTrain[0:int(len(xTrain)*TRAIN_PORCENTAGE)]

		yTrain = xTrain.pop("final_result")
		yTest = xTest.pop("final_result")

		xTrain = pd.get_dummies(xTrain)
		yTrain = pd.get_dummies(yTrain)

		xTest = pd.get_dummies(xTest)
		yTest = pd.get_dummies(yTest)	

		return (xTrain, yTrain, xTest, yTest)

	@staticmethod
	def __requestDataset():
		return pd.read_csv(PROJECT_ROOT+"/datasets/studentInfo.csv")