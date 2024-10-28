
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    reduce_scatter_1 = tf.raw_ops.ReduceScatter(x1, name='ReduceScatter_1', section=[3], row_dim=1, col_dim=1)
    reduce_scatter_2 = tf.raw_ops.ReduceScatter(x2, name='ReduceScatter_2', section=[3], row_dim=1, col_dim=1)
    sum_1 = tf.raw_ops.Add(reduce_scatter_1, reduce_scatter_2, name='Add_1')
    sum_2 = tf.raw_ops.Add(x1, sum_1, name='Add_2')
    return tf.raw_ops.ReduceScatter(sum_2, name='ReduceScatter_3', section=[3], row_dim=1, col_dim=1)

# Initializing the model
n = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([[[1,2,3,4]]], dtype=tf.float32, shape=[1,1,4])
x2 = tf.constant([[[5,6,7,8]]], dtype=tf.float32, shape=[1,1,4])
x3 = tf.constant([[[9,10,11,12]]], dtype=tf.float32, shape=[1,1,4])

# Call model
y = n(x1, x2)