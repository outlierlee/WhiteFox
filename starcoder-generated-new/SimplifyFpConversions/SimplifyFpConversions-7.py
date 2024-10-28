
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.cast(x1, tf.float32)
    x3 = tf.cast(x2, tf.float64)
    return tf.cast(x3, tf.int32)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
```
In the provided solutions, usage of private TensorFlow APIs is explicitly isolated. The tf namespace is even explicitly mentioned so as not to use any internal or private TensorFlow APIs. The solutions are not meant to be the final and optimized version of the code, but meant to be test-able and use as a starting point for the creation of a final versions.