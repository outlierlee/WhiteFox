:
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    w1 = tf.Variable(tf.random.normal(shape=[256, 256]))
    w2 = tf.Variable(tf.random.normal(shape=[256, 10]))
    x2 = tf.random.normal(shape=[256, 256])
    y = tf.tensordot(x1, w1, axes=1)
    return tf.tensordot(y, w2, axes=1)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [256]
x1 = tf.constant(tf.random.normal(shape=input_shape), tf.float32)

# Call model
y = m(x1)