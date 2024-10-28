
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.broadcast_to(x1, [1])
    return tf.reshape(x2, [])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [1]
x1 = tf.constant([2.], shape=input_shape)

# Call model
y = m(x1)
```