
class Model(tf.keras.Model):

  def __init__(self, rhs0, rhs1, lhs):
    super(Model, self).__init__()
    self.rhs0 = rhs0
    self.rhs1 = rhs1
    self.lhs = lhs

  def call(self):
    dot0 = tf.linalg.matmul(self.lhs, self.rhs0)
    dot1 = tf.linalg.matmul(self.lhs, self.rhs1)
    return dot0, dot1

# Initializing the model
lhs = tf.constant([[1,2,3],[4,5,6]])
rhs0 = tf.constant([[7,8],[9,10],[11,12]])
rhs1 = tf.constant([[13,14],[15,16],[17,18]])
m = Model(rhs0, rhs1, lhs)

dot0, dot1 = m()