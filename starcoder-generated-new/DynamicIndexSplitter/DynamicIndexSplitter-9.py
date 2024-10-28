
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, indices):
    return tf.dynamic_update_slice(x1, [1.0], indices)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2, 2]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
indices = tf.constant([0, 0], shape=[2])

# Call model
y = m(x1, indices)
```

Please generate multiple valid TensorFlow models that satisfy both requirements as shown below.

# Multiple Models
```
