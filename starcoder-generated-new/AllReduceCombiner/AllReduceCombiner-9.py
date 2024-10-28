

class Model(tf.keras.Model):

  def __init__(self, threshold_in_bytes, threshold_count):
    super(Model, self).__init__()
    self.reduce_sum = tf.raw_ops.AllReduce
    self.combine_threshold_in_bytes_ = threshold_in_bytes
    self.combine_threshold_count_ = threshold_count

  def call(self, *args):
    reduced_values = [self.reduce_sum(arg) for arg in args]
    return reduced_values

# Initializing the model
m = Model(1024, 10)

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x2 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x3 = tf.constant([4.,5.,6.,7.], shape=input_shape)
# Call model
y = m(x1, x2, x3)