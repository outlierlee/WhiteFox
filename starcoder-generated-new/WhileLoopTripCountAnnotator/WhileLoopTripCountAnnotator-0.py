
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    i = tf.constant(0)
    c = lambda i: tf.math.logical_and(tf.less(i, x), tf.greater(x, i))
    b = lambda i: tf.add(i, 1)
    tf.while_loop(c, b, [i])
    return tf.constant(0)
    
# Initializing the model
m = Model()

# Inputs to the model
input_shape = [1]
x = tf.constant([10.], shape=input_shape)

# Call model
y = m(x)