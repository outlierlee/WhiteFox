
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    async_start = tf.xla.experimental.start_async_outbound_data_transfer(x1)
    async_done = tf.xla.experimental.done_async_outbound_data_transfer(async_start)
    return async_done

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [1]
x1 = tf.constant([200.], shape=input_shape)

# Call model
y = m(x1)

# Just printing the y (which should also be x1 if we have no ops between start and end)
print(y)