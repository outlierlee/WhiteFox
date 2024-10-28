
class Model(tf.keras.Model):

  def __init__(self, dtype):
    super(Model, self).__init__()
    self.dtype = dtype

  def call(self, x1):
    x2 = tf.cast(x1, dtype=self.dtype)
    return x2

# Initializing the model
dtype = tf.float32
m = Model(dtype=dtype)

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)

print(y)
```

You can replace the data type accordingly (`tf.float32`, `tf.int32`, `tf.float64`, etc.) to generate different models.