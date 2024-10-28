
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, lhs, rhs):
    return tf.linalg.batch_matmul(lhs, rhs, adj_x=True)

# Inputs to the model   
lhs = tf.constant([[1.1],[2.2],[3.3],[4.4]])
rhs = tf.constant([[5.5, 6.6, 7.7],[8.8, 9.9, 0.0]])

# Call model
result = Model()(lhs, rhs)

# Output
print(result)