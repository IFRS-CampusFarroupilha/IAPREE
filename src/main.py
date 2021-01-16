from data.student import studentDataset
from utils.functions import inject
from modules.dense import DenseModule
import colorama

def main():
	colorama.init()

	xTrain, yTrain, xTest, yTest = studentDataset.getDataset()

	ia = ["dense", "dense"]

	inject(ia, DenseModule.getModule())

	print(xTrain, yTrain, xTest, yTest, ia)

if __name__ == "__main__":
	main()
