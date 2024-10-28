
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    axis = 1
    concat_1 = tf.concat([x1, x2], axis)
    return tf.concat([concat_1, x1], axis)

# Initializing the model
m = Model()

# Inputs to the model
input_shape=[4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x2 = tf.constant([4.,2.,6.,1.], shape=input_shape)

# Call model
y = m(x1, x2)