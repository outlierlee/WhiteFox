

Assuming we have a 2-dimensional input tensor and want to extract a slice of its first row, we can define the following model using dynamic slicing:

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    return tf.dynamic_slice(x1, [0, 0], [1, -1])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2,3]
x1 = tf.constant([[1.,2.,3.],[4.,5.,6.]], shape=input_shape)

# Call model
y = m(x1)

# Expected output
y_expected = tf.constant([[1.,2.,3.]])