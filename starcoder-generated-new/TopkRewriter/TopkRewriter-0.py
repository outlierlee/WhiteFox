
class Model(tf.keras.Model):
    
  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    sorted_tensor = tf.sort(x, axis=-1, direction='DESCENDING')
    return tf.slice(sorted_tensor, [0, 0], [-1, 2])

# Initializing the model
m = Model()

# Inputs to the model
x = tf.constant([[1.0, 3.0, 2.0], [4.0, 6.0, 5.0]])

# Call model
y = m(x)

print(y)