
```python
class Model(tf.keras.Model):
  def __init__(self, reduce_window_size_):
    super(Model, self).__init__()
    self.reduce_window_size_ = reduce_window_size_
  
  def call(self, x1):
    # For optimizing the tf.reduce_sum
    return tf.reduce_sum(x1, axis=[0, 1])

# Initializing the model
m = Model(reduce_window_size_=2)

# Inputs to the model
input_shape = [4, 4]
x1 = tf.constant([4.,5.,6.,7.,4.,5.,6.,7.,4.,5.,6.,7.,4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
```