:
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    return tf.raw_ops.StochasticConvert(x1, x2)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([3.7, 0.2, 4.9, 1.6], shape=input_shape)
x2 = tf.constant([0.1, 0.4, 0.7, 0.9], shape=input_shape)

# Call model
y = m(x1, x2)
```