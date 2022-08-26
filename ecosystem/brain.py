import tensorflow as tf
import numpy as np

class Brain:

	def __init__(self, inputs, outputs):
		self.W1 = tf.Variable(tf.random.truncated_normal([inputs, 5], stddev=0.1), dtype=tf.float32)	
		self.b1 = tf.Variable(tf.random.truncated_normal([1, 5], stddev=0.1), dtype=tf.float32)	
		self.W2 = tf.Variable(tf.random.truncated_normal([5, outputs], stddev=0.1), dtype=tf.float32)	
		self.b2 = tf.Variable(tf.random.truncated_normal([1, outputs], stddev=0.1), dtype=tf.float32)	
	
	def feedforward(self, perceptions):
		if len(perceptions) <= 0:
			return np.array([0,0])

		# For now, get the closest food info
		perception = perceptions[0]
		perception_list = []

		# Transform the dict perception into a list of floats
		for k in perception:
			perception_list.append(perception[k])
		
		perception_tf = tf.constant([perception_list], dtype=tf.float32)

		h1 = tf.sigmoid(tf.matmul(perception_tf, self.W1) + self.b1) 
		y = tf.tanh(tf.matmul(h1, self.W2))
		return y.numpy()[0]