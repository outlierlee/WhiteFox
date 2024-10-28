
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x = tf.sort(x1, direction = "DESCENDING")
    x = tf.slice(x, [0, 0], [-1, 2])
    return tf.negative(x)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2, 3]
x = tf.constant([1.0, 3.0, 2.0, 4.0, 6.0, 5.0], shape=input_shape)

# Call model
y = m(x)

