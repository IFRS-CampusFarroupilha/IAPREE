from data.student import studentDataset
from utils.functions import inject
from modules import dense, dropout
import tensorflow as tf
import colorama

def main():
	colorama.init()

	xTrain, yTrain, xTest, yTest = studentDataset.getDataset()

	layers = studentDataset.getStart()
	inject(layers, dense.DenseModule.getModule(6))
	inject(layers, dropout.DropOutModule.getModule())
	inject(layers, studentDataset.getEnd())

	model = tf.keras.Sequential(layers)


	model.compile(
		optimizer=studentDataset.getBestOptimizer(),
		loss=studentDataset.getBestLoss(),
		metrics=['acc']
	)

	history = model.fit(xTrain, yTrain, epochs=100)

	print(history)

if __name__ == "__main__":
	main()
