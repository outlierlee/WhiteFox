
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    x3 = tf.multiply(x1, tf.transpose(x2, perm=[0,2,1]))
    return tf.tensordot(x3, x2, axes=[[1], [1]])

# Initializing the models
m = Model()

# Inputs to the model
input_shape = [2,2,2]
x1 = tf.constant([[1.,2.],[3.,4.]], shape=input_shape)
x2 = tf.constant([[1.,2.]], shape=input_shape[:-1])

# Call model
y = m(x1, x2)

