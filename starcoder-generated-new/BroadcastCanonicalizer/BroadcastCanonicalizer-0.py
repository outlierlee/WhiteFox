
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    return tf.broadcast_to(x1, [2,3,4])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2,2]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)