
class Model(tf.keras.Model):
    
  def __init__(self):
    super(Model, self).__init__()

  def true_fn(self):
    return tf.constant(1)

  def false_fn(self):
    return tf.constant(0)

  def call(self, x):
    return tf.cond(tf.constant(True), self.true_fn, self.false_fn)


# Initializing the model
m = Model()

# Call model
y = m(None)

# Expected output: y = 1