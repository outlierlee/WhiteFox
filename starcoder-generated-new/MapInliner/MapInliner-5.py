:
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    def func(x):
        return tf.math.abs(x)
    
    return tf.map_fn(func, x1)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([-1, 0, 1, 2], shape=input_shape)

# Call model
y = m(x1)