
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

    self.y = tf.constant(np.array([1, 2, 3]))  # invariant instruction

  def call(self, x):
    @tf.function
    def cond(x):
      return tf.add(tf.reduce_sum(x), tf.reduce_sum(self.y)) < 1000

    def body(x):
      y = x + self.y
      return y

    result = tf.while_loop(cond, body, [x])
    return result

# Initializing the model
m = Model()

# Inputs to the model
x = tf.constant(np.array([1, 2, 3]))

# Call model
y = m(x)