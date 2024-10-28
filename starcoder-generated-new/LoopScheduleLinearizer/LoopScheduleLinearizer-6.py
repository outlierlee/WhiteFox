
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    for _ in range(10):
      # read operation
      read = tf.reduce_mean(x)

      # write operation
      x = tf.raw_ops.Assign(ref=x, value=read)
      
    return x

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)