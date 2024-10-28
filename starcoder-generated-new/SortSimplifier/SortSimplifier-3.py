
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    # Sort the input tensors and only use the first two outputs
    sorted_tuple = tf.sort(x)
    return some_function(sorted_tuple[0], sorted_tuple[1])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2,2]
x = (tf.constant([4.,5.], shape=input_shape), tf.constant([1.,2.], shape=input_shape))

# Call model
y = m(x)