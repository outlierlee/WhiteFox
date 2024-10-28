
class Model(tf.keras.Model):
    
  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    x1 = tf.cast(x, tf.bfloat16)
    return tf.cast(x1, tf.float32)

# Initializing the model
m = Model()

# Inputs to the model
x = tf.constant([4.0, 5.0, 6.0, 7.0])

# Call model
y = m(x)