
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    t1 = tf.raw_ops.ReduceScatter(x1, y1, op="SUM")
    t2 = tf.raw_ops.ReduceScatter(tf.cast(tf.constant(2, shape=[4]), tf.int32) * x2, y2, op="SUM")
    t3 = tf.raw_ops.ReduceScatter(t1 + t2, z, op="SUM")
    return t3

m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([1.,2.,3.,4.], shape=input_shape)
x2 = tf.constant([2.,4.,6.,8.], shape=input_shape)

y1 = tf.constant([3.,5.,7.,9.], shape=input_shape)
y2 = tf.constant([5.,8.,4.,1.], shape=input_shape)

z = tf.constant([6.,8.,3.,9.], shape=input_shape)

# Call model
y = m(x1, x2)
```