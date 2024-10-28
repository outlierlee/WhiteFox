
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    return tf.broadcast_to(x, [3, 4, 4])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4, 4]
x = tf.constant([1,2,1,2], shape=input_shape)

# Call model
y = m(x)
```