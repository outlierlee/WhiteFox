

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def body(self, x):
    # read operation
    read = tf.reduce_sum(x)
    # write operation
    write = tf.assign(x, read)
    return write

  def call(self, x):
    x = self.body(x)
    result = tf.while_loop(lambda x: tf.less(x, 10), self.body, [x])
    return result

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x)