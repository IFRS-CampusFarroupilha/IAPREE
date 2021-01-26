from modules.module import Module
import tensorflow as tf

class DropOutModule(Module):

	information = {
		"author":"Otávio",
		"yearReleased":"2020",
		"source":"Me",
		"description":"Just add an dropout"
	}

	@staticmethod
	def getModule():
		l = tf.keras.layers
		
		return [
			l.Dropout(0.5)
		]
