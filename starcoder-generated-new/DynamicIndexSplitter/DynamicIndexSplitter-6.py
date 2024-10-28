
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, start_indices, slice_sizes):
    return tf.dynamic_slice(x1, start_indices=start_indices, slice_size=slice_sizes)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
start_indices = tf.constant([1, 1], shape=[2])
slice_sizes = tf.constant([2, 2], shape=[2])

# Call model
y = m(x1, start_indices, slice_sizes)
```
The optimization pass `AVX512FxxDTypeSplit` in TensorFlow XLA is responsible for splitting operations and broadcasting which utilizes the `xx` prefix on the function names. You can take inspiration from this one to split certain operations into simpler ones and hence improving the output TensorFlow XLA IR compatible with the TensorRT compiler.