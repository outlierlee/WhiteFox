
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    self.m = tf.constant([4.,5.,6.,7.], dtype=tf.float32)

  def call(self, x1):
    x2 = tf.convert_to_dtype(x1, tf.float64)
    return tf.reshape(x2, [2,2])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
```