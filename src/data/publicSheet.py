from utils.consts import TRAIN_PORCENTAGE, PROJECT_ROOT
from data.dataset import Dataset
from io import StringIO
import tensorflow as tf
import pandas as pd
import requests

class publicDataset(Dataset):

	information = {
		"title": "Public Dataset for IAPREE",
		"author": "IFRS",
		"yearReleased":"2021",
		"source":"https://docs.google.com/spreadsheets/d/e/2PACX-1vSwe_5dZINGg-usxfyW6iS7akHETzaM9PsTLzxIN2zxMyRdhPkzD1fUzEtVUvhu1BHmdwbtvvBI4VNO/pub?output=csv",
		"description":"Contains data from the public IAPREE dataset"
	}

	@staticmethod
	def getBestOptimizer():
		""" Gets the best of the AI if you use this dataset """
		return tf.keras.optimizers.Adam()

	@staticmethod
	def getBestLoss():
		""" Gets the start of the AI if you use this dataset """
		return tf.keras.losses.categorical_crossentropy


	@staticmethod
	def getStart():
		return [tf.keras.layers.Dense(10, input_shape=[2,])]

	@staticmethod
	def getEnd():
		return [tf.keras.layers.Dense(4, activation="softmax")]

	@staticmethod
	def getDataset():
		xTrain = publicDataset.__requestDataset()
		
		xTest = xTrain[int(len(xTrain)*TRAIN_PORCENTAGE)+1:len(xTrain)]
		xTrain = xTrain[0:int(len(xTrain)*TRAIN_PORCENTAGE)]

		yTrain = xTrain.pop("data")
		yTest = xTest.pop("data")

		xTrain = pd.get_dummies(xTrain)
		yTrain = pd.get_dummies(yTrain)

		xTest = pd.get_dummies(xTest)
		yTest = pd.get_dummies(yTest)	

		return (xTrain, yTrain, xTest, yTest)

	@staticmethod
	def __requestDataset():
		request = requests.get(publicDataset.information["source"], allow_redirects=True)
		formatted = request.content.decode("utf-8")

		data = pd.read_csv(StringIO(formatted))

		return data