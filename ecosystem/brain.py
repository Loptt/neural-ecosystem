import tensorflow as tf

class Brain:

	def __init__(self):
		self.W1 = tf.Variable(tf.random.truncated_normal([1, 5], stddev=0.1))	
		self.b1 = tf.Variable(tf.random.truncated_normal([1, 5], stddev=0.1))	
		self.W2 = tf.Variable(tf.random.truncated_normal([5, 2], stddev=0.1))	
		self.b2 = tf.Variable(tf.random.truncated_normal([1, 2], stddev=0.1))	
	
	def feedforward(self, perception):
		h1 = tf.sigmoid(tf.matmul(perception, self.W1) + self.b1) 
		y = tf.matmul(h1, self.W2)