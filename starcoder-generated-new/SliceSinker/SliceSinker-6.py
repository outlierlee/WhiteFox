
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    x3 = tf.slice(x1, [0], [2])
    x4 = tf.slice(x1, [2], [2])
    res = tf.add(x3, x4)
    return res

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x2 = tf.constant([0.,0.,0., 0.], shape=input_shape)

# Call model
y = m(x1, x2)