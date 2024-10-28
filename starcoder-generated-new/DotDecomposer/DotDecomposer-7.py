
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    return tf.tensordot(x1, x2, axes=[[1, 2], [0, 1]])

# Initializing the model
m = Model()

# Inputs to the model
input_shape1 = [2,2]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape1)
input_shape2 = [2,2]
x2 = tf.constant([34., 43., 52., 61.], shape=input_shape2)

# Call model
y = m(x1, x2)


