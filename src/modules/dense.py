from modules.module import Module
import tensorflow as tf

class DenseModule(Module):

	information = {
		"author":"Otávio",
		"yearReleased":"2020",
		"source":"Me",
		"description":"Process the information using dense layeres"
	}

	@staticmethod
	def getModule(multiplier=10):
		l = tf.keras.layers

		return [
			l.Dense(2**multiplier, activation="relu"),
			l.Dense(2**multiplier-1, activation="relu")
		]
