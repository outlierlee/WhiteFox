
class Model(tf.keras.Model):
    
  def __init__(self):
    super(Model, self).__init__()
    self.lhs = tf.Variable([[1., 1.], [1., 1.]])
    self.rhs0 = tf.Variable([[2., 2.], [2., 2.]])
    self.rhs1 = tf.Variable([[3., 3.], [3., 3.]])

  def call(self, x):
    dot0 = tf.linalg.matmul(self.lhs, self.rhs0)
    dot1 = tf.linalg.matmul(self.lhs, self.rhs1)
    return dot0, dot1

m = Model()
x = tf.constant([[1., 2.], [3., 4.]])
d0, d1 = m(x)