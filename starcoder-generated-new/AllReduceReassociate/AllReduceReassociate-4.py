
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.reduce_all(x1, [1])
    x3 = tf.reduce_all(x1, [1])
    return tf.maximum(x2, x3)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [3, 4]
x1 = tf.constant([4.,5.,6.,7., 3.,4.,5.,6., 2.,3.,4.,5.], shape=input_shape)

# Call model
y = m(x1)
# Expected output: [6., 7.]