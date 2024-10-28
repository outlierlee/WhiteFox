

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):

    @tf.function(experimental_autograph=True)
    def condition(*args):
      return tf.reduce_any(args[0] < 3)

    @tf.function(experimental_autograph=True)
    def body(*args):
      return tf.add(args[0], 1), args[1]

    return tf.while_loop(condition, body, [x1, 2])

# Initializing the model
m = Model()

# Inputs to the model
x1 = tf.constant(0)

# Call model
y = m(x1)