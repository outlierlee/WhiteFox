
class Model(tf.keras.Model):
    
  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    return tf.xla.experimental.reduce_scatter(x, [[1, 1]])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2, 2]
comm_spec_shape = [2] # Each takes 1 dimension but all together are 2 (devices=comm_size)
x = tf.constant([[1., 2.], [3., 4.]], shape=input_shape)

# Validate Reduce-Scatter where device count equals input size
try:
  m(x)
  exception = None
except Exception as e:
  exception = e
  
assert exception is None, f"Expected valid reduce-scatter but got an error: {exception}"