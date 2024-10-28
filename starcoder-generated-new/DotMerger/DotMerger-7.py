
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.reshape(x1, [2,2])
    return tf.reshape(x2, [4])

# Initializing the model
m = Model()

# Inputs to the model
lhs = tf.Variable([[1., 2.], [3., 4.]], dtype=tf.float32)
rhs0 = tf.Variable([[1., 2.], [3., 4.]], dtype=tf.float32)
rhs1 = tf.Variable([[1., 2.], [3., 4.]], dtype=tf.float32)

# Call model
y = tf.linalg.matmul(lhs, rhs0)
z = tf.linalg.matmul(lhs, rhs1)

print(y)
print(z)