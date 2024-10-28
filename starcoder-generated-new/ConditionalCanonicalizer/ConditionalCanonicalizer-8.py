
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    def true_fn():
      return tf.constant(1.0)

    def false_fn():
      return tf.constant(0.0)

    return tf.cond(tf.constant(True), true_fn, false_fn)

# Initializing the model
m = Model()

# Inputs to the model
x1 = tf.constant([4.,5.,6.,7.])

# Call model
y = m(x1)

# Print output
print(y)