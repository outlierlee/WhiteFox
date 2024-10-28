
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, lhs, rhs):
    return tf.linalg.batch_matmul(lhs, rhs)
    
# Initializing the model
m = Model()

# Inputs to the model
lhs_shape = [2, 1, 4, 3]
lhs = tf.random.normal(lhs_shape)
rhs_shape = [2, 3, 5, 7]
rhs = tf.random.normal(rhs_shape)

# Call model
y = m(lhs, rhs)
```