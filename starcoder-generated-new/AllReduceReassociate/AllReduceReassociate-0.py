
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    x1_reduce = tf.raw_ops.AllReduce(
    inputs=tf.cast(x1, tf.float32),
    reduction=Reduction.MIN,
    group_assignment=[1],
    keep_dims=True)

    x2_reduce = tf.raw_ops.AllReduce(
    inputs=tf.cast(x2, tf.float32),
    reduction=Reduction.MAX,
    group_assignment=[1],
    keep_dims=True)

    return x1_reduce + x2_reduce

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x2 = tf.constant([1.,2.,3.,8.], shape=input_shape)

# Call model
y = m(x1, x2)