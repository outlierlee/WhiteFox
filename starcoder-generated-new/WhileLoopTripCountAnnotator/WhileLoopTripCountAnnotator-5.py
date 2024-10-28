
Class Model(tf.keras.Model):
  
  def __init__(self):
    super(Model, self).__init__()
  
  def call(self, x):
    i = tf.constant(0)
    c = lambda i: tf.less(i, x)
    b = lambda i: tf.add(i, 1)
    r = tf.while_loop(c, b, [i])
    return r

# Initializing the model
m = Model()

# Call model
x = tf.constant(10)
y = m(x)