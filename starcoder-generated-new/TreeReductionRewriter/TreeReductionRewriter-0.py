
class Model(tf.keras.Model):

  def __init__(self, reduce_window_size):
    super(Model, self).__init__()
    self.reduce_window_size = reduce_window_size

  def call(self, x):
    # Define arbitrary shape that has at least one dimension > reduce_window_size_
    if x.shape[0] > self.reduce_window_size:
      return tf.reduce_sum(x, axis=0)
    else:
      return tf.reduce_sum(x, axis=[0, 1])

# Initializing the model
m = Model(reduce_window_size_=20)

# Inputs to the model
input_shape = [40,20,10]
x = tf.constant(np.random.randn(*input_shape), shape=input_shape)

# Call model
y = m(x)
```

In the above example, the second reshape is "activated" if the first dimension of the `input_tensor` (`x`) is larger than `reduce_window_size=20`.