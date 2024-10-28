
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.constant([4.,5.,6.,7.], dtype=tf.float32) # constant operand
    y1 = tf.add(x2, tf.Variable([5.0, 6.0, 7.0, 8.0], trainable=True)) # dependent variable
    return x1 + y1

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)


