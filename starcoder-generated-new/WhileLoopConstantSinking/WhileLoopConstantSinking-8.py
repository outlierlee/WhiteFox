

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    i = tf.constant(0)
    while tf.reduce_any(i < 10):
      i = tf.add(i, 1)
    return i + 1

m = Model()
x = tf.constant(0)
m(x)