
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    return tf.linalg.batch_matmul(x1, x2, adjoint_a=False, adjoint_b=False)

# Initializing the model
m = Model()

# Inputs to the model
lhs_shape = [2, 1, 4, 5]
rhs_shape = [2, 3, 5, 6]
x1 = tf.random.normal(lhs_shape)
x2 = tf.random.normal(rhs_shape)

# Call model
y = m(x1, x2)