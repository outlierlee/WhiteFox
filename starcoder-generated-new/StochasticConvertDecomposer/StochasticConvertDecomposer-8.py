
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, y1):
    x1 = tf.cast(x1, tf.float64)
    y = tf.raw_ops.StochasticConvert(x1, y1)
    return y

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
y1 = tf.constant([0.1,0.2,0.3,0.4], shape=input_shape) 

# Call model
y = m(x1, y1)