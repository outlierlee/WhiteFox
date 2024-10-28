
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x1 = tf.sort(x1, direction="DESCENDING", stable=True)
    return tf.slice(x1, [0, 0], [-1, 2])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2,3]
x1 = tf.constant([[1.0, 3.0, 2.0], [4.0, 6.0, 5.0]], shape=input_shape)

# Call model
y = m(x1)