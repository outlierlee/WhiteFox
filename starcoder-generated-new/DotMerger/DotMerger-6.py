
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    self.lhs = tf.Variable([[1,0],[0,1]], dtype='float32')
    self.rhs0 = tf.Variable([[1],[1]], dtype='float32')
    self.rhs1 = tf.Variable([[0],[0]], dtype='float32')

  def call(self, x):
    return tf.linalg.matmul(self.lhs, self.rhs0), tf.linalg.matmul(self.lhs, self.rhs1)

# Initializing the model
m = Model()

# Call model
y1, y2 = m(None)
print(y1)
print(y2)