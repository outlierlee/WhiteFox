
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    x = tf.math.add(x, x)
    x = tf.math.multiply(x, x)
    return x

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x)
```

Please note, TensorFlow XLA’s `Defuser` optimization pass requires the TensorFlow compiler to be used for compilation.

Please follow and run TensorFlow's guide on XLA compilation for simple models (https://www.tensorflow.org/xla/get_started?hl=en) to enable and run the models on TensorFlow XLA.