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
	def getModule():
		l = tf.keras.layers
		return [
			l.Dense(512, activation="relu"),
			l.Dense(256, activation="relu")
		]
