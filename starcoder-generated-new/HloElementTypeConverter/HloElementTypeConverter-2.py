
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x, y):
    x = tf.cast(x, tf.int32)
    y = tf.cast(y, tf.int32)
    z = tf.add(x, y)
    return z

# Initialize the model
m = Model()

# Inputs to the model
x = tf.constant([1, 2, 3], dtype=tf.float32)
y = tf.constant([1, 2, 3], dtype=tf.float32)

# Call model
z = m(x, y)
```
Please provide one such model.