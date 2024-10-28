
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    start_indices = tf.constant([2])
    slice_sizes = tf.constant([2])
    return tf.dynamic_slice(x1, start_indices, slice_sizes)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
```

Note: Above examples are python script. You also can run them directly in Jupyter Notebook or similar environments.