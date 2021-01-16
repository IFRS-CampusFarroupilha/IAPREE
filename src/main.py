from data.student import studentDataset
import colorama

def main():
	colorama.init()

	dataset = studentDataset()
	xTrain, yTrain, xTest, yTest = dataset.getDataset()


	print(xTrain, yTrain, xTest, yTest)

if __name__ == "__main__":
	main()