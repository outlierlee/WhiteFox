
class Model(tf.keras.Model):

  def __init__(self, reduce_window_size_):
    super(Model, self).__init__()
    self.reduce_window_size_ = reduce_window_size_

  def call(self, x1):
    ## Setting up x1 as input tensor of shape 4x4 to match the reductions we are doing in case they are relevant for the conditions.
    return tf.reduce_sum(x1, axis=[0, 1])


# Initializing the model with arbitrary values larger than the dimensions of x1
m = Model(reduce_window_size_=5)

# Inputs to the model
input_shape = [5, 4]
x1 = tf.ones(input_shape)

# Call model
y = m(x1)
```

