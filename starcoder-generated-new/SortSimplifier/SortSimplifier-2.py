
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2, x3):
    sorted_tuple = tf.sort((x1, x2, x3))
    return self.some_function(sorted_tuple[0], sorted_tuple[1])

  def some_function(self, x1, x2):
    return x1 + x2

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x2 = tf.constant([1.,2.,3.,8.], shape=input_shape)
x3 = tf.constant([9.,8.,7.,6.], shape=input_shape)

# Call model
y = m(x1, x2, x3)