
class Model(tf.keras.Model):
    
  def __init__(self):
    super(Model, self).__init__()
    self.dummy = tf.Variable(0.)

  def call(self, x1):
    x3 = tf.add(x1, 10)
    return x2

m = Model()
x1 = tf.constant(1., shape=())
y = m(x1)