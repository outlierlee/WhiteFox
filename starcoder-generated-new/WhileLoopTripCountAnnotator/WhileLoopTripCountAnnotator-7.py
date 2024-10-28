
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    i = tf.constant(0)
    c = lambda i: tf.less(i, 5)
    b = lambda i: tf.add(i, 1)
    return tf.while_loop(c, b, [i])

# Initializing the model
m = Model()

# Inputs to the model
x = tf.constant(0)

# Call model
output = m(x)
print(output)