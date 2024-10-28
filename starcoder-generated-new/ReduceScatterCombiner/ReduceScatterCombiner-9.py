

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2, x3, x4):
    y1 = tf.raw_ops.ReduceScatter(input=x1, reduction_op='add')
    y2 = tf.raw_ops.ReduceScatter(input=x2, reduction_op='add')
    y3 = tf.raw_ops.ReduceScatter(input=x3, reduction_op='add')
    y4 = tf.raw_ops.ReduceScatter(input=x4, reduction_op='add')
    return y1 + y2 + y3 + y4

# Initializing the model
m = Model()

# Inputs to the model
X_shape = [16]
x1 = tf.ones(shape=X_shape, dtype=tf.int32)
x2 = tf.ones(shape=X_shape, dtype=tf.int32)
x3 = tf.ones(shape=X_shape, dtype=tf.int32)
x4 = tf.ones(shape=X_shape, dtype=tf.int32)

# call model
y = m(x1, x2, x3, x4)