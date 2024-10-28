
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

    self.i = tf.Variable(0, trainable=False)

  def call(self, x):
    
    def loop_body(i):
      x = tf.add(i, 1)
      return tf.add(i, 1)
    
    def loop_exit(i):
      return tf.less(i, 10)

    _, x = tf.while_loop(loop_exit, loop_body, [self.i])

    self.i = x
    return x

# Initializing the model
m = Model()

# Inputs to the model
x1 = 0

# Call model
y = m(x1)