
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.broadcast_to(x1, [1,7])
    return tf.reshape(tf.nn.all_gather(x2, (1,2,5,6,7)), [7,1,5,6,7])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [7]
x1 = tf.constant([4.,5.,6.,7.,1.,2.,3.], shape=input_shape)

# Call model
y = m(x1)