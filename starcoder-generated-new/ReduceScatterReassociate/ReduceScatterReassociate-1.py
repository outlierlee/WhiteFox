
class MyModel(tf.keras.Model):

  def __init__(self):
    super(MyModel, self).__init__()

  def call(self, x1, x2):
    # initial reduction operation which would not cause the ReduceScatterReassociate pass
    x3 = tf.reduce_mean([x1, x2], axis=0)
    x4 = tf.sparse.sparse_dense_matmul(x3, x3)
    # reduce scatter
    x5 = tf.raw_ops.ReduceScatter(x4, [1], tf.multiply)
    x6 = tf.raw_ops.ReduceScatter(x4, [0], tf.multiply)
    return x5 + x6

# Initializing the model
m = MyModel()

# inputs to the model
input_shape = [2,2]
x1 = tf.constant([1.,1.,2.,2.], shape=input_shape)
x2 = tf.constant([3.,3.,4.,4.], shape=input_shape)

# supports 2 different computation paths
y = m(x1, x2)