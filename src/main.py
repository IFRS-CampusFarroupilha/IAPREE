from data.publicSheet import publicDataset
from utils.functions import inject
from modules import dense, dropout
from callbacks.ReachAccuracyStop import ReachAccuracyStop
import tensorflow as tf
import colorama

def main():
	colorama.init()

	dataset = publicDataset

	xTrain, yTrain, xTest, yTest = dataset.getDataset()

	reachAccuracyStop = ReachAccuracyStop(0.85)

	layers = dataset.getStart()
	inject(layers, dense.DenseModule.getModule(6))
	inject(layers, dropout.DropOutModule.getModule())
	inject(layers, dataset.getEnd())

	model = tf.keras.Sequential(layers)

	model.compile(
		optimizer=dataset.getBestOptimizer(),
		loss=dataset.getBestLoss(),
		metrics=['acc']
	)

	history = model.fit(
		xTrain,
		yTrain, 
		epochs=100,
		callbacks=[
			reachAccuracyStop
		]
	)

	print(history.history["acc"])

if __name__ == "__main__":
	main()
