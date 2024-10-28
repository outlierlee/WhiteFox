
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    self.add = tf.add
    self.multiply = tf.multiply

  def call(self, x):
    x = self.add(x, x)
    y = self.multiply(x, x)
    return y

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x)

# The effect of compilation to TensorFlow's XLA is listed below. A new operation named DEFUSER_BUILD_FUSION is created in the compilation's representation. This special operation represents the final version of the fusion operation residing in the original computation, i.e. (x + x) * (x + x):
```