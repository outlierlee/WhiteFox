
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    def true_fn():
      return tf.constant(1)

    def false_fn():
      return tf.constant(0)

    return tf.cond(tf.constant(True), true_fn, false_fn)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x)
print(y)