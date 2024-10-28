
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    t1 = tf.slice(x1, [0], [-1])
    t2 = tf.slice(x2, [0], [-1])
    t3 = t1 + t2
    return t3

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x2 = tf.constant([1.,2.,3.,4.], shape=input_shape)

# Call model
y = m(x1, x2)