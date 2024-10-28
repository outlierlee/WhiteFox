
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    self.lhs = tf.Variable([[1., 2.], [3., 4.]])
    self.rhs0 = tf.Variable([[5., 6.], [7., 8.]])
    self.rhs1 = tf.Variable([[9., 10.], [11., 12.]])

  def call(self):
    dot0 = tf.linalg.matmul(self.lhs, self.rhs0)
    dot1 = tf.linalg.matmul(self.lhs, self.rhs1)
    return dot0, dot1

# Initializing the model
m = Model()

# Call model
res = m()
```

This model is divided into two matrices - `lhs` and `rhs*` - which are multiplied to each other and results are returned. So, this represents a dot operation pattern as required.