
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.pad(x1, [[1,1], [1,1]])
    return tf.convert_to_dtype(x2, tf.float64)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2, 2]
x1 = tf.constant([1.,2.], shape=input_shape)

# Call model
y = m(x1)

In both models, the higher precision data types are taken as `float64` and the lower precision data types are taken as `float32`.

The converted representation of a tensor should be still losslessly recoverable to its original representation after the `ConvertMover` optimization pass in TensorFlow XLA.