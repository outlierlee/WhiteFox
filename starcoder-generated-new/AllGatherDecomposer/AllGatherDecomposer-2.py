

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    # Assume that `should_decompose_(self, op)` is a function
    # as described in the `should_decompose_` commentary.
    x2 = tf.raw_ops.AllGather(..., should_decompose_(self, op))
    return x2

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)