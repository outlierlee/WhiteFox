
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    self.cc = tf.raw_ops.CollectiveCommunications(...)

  def call(self, x1):
    all_reduce_handle = self.cc.all_reduce(x1)
    return self.cc.all_reduce_done(all_reduce_handle)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)