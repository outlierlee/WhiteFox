
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    start_indices = tf.constant([1, 2])
    slice_sizes = tf.constant([2, 2])
    
    x2 = tf.dynamic_slice(x1, start_indices, slice_sizes)
    
    update = tf.constant([10., 11., 12., 13.], shape=[4])
    start_indices = tf.constant([1, 2])
    
    x3 = tf.dynamic_update_slice(x1, update, start_indices)
    
    return x3

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)

