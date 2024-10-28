
# TODO

# FYI: The following code is an incorrect substitution, you should replace it.
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x, y):
    t1 = tf.add(x, y)
    return t1

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x2 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1, x2)
```