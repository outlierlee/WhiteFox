
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    counter = tf.constant([0, 0, 0, 0], dtype=tf.int32)
    value = tf.constant([1, 2, 3], dtype=tf.int32)
    z = x
    while tf.reduce_sum(z) < 1000:
      y = tf.add(z, value)
      z = y  # invariant instruction
      counter = tf.add(counter, 1)
    return counter

# Initializing the model
m = Model()

# Inputs to the model
x = tf.constant(np.array([1, 2, 3]), dtype=tf.int32)

# Call model
y = m(x)