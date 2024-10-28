
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, start_indices, slice_sizes):
    return tf.dynamic_update_slice(x1, tf.cast(slice_sizes, tf.float32), start_indices)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2,2]
x1 = tf.constant([[1.,2.],[3.,4.]], shape=input_shape)
start_indices_shape = [2]
slice_sizes_shape = [2,2]

start_indices = tf.constant([0, 0], shape=start_indices_shape)
slice_sizes = tf.constant([[0., 0.], [3., 3.]], shape=slice_sizes_shape)

# Call model
y = m(x1, start_indices, slice_sizes)