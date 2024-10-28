
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    start_indices = tf.constant([1,1])
    slice_sizes = tf.constant([2,2])
    x2 = tf.dynamic_slice(x1, start_indices, slice_sizes) # Vector indices use dynamic_slice
    return x2

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4,4]
x1 = tf.Variable(np.ones(input_shape))

# Call model
y = m(x1)

# Model generates an error can't use tf.dynamic_slice/tf.dynamic_update_slice with non-scalar start indices
x1 = tf.Variable(np.ones([3,3]))
m(x1) # Error: dimension must be Scalar
```