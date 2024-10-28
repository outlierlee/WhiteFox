
class Model(tf.keras.Model):
    
  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    sorted_tuple = tf.sort(x)
    return some_function(sorted_tuple[0], sorted_tuple[1])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2]
x = (tf.constant([2.,1.], shape=input_shape), tf.constant([3.,4.], shape=input_shape), tf.constant([5.,6.], shape=input_shape))

# Call model
x = m(x)