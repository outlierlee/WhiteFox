
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    input_shape =  [2, 1, 10]
    x2 = tf.constant([4.,5.,6.,7.], shape=input_shape)
    new_shape = [2,7,10]
    x3 = tf.broadcast_to(x2, new_shape)
    return x3

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [10]
x1 = tf.constant([0,2], shape=input_shape)

# Call model
y = m(x1)