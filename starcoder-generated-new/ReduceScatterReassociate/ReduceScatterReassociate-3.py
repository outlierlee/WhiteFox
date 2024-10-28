
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    t1 = tf.reduce_sum(x1)
    t1 += x2
    t2 = tf.reduce_sum(t1)
    return tf.raw_ops.ReduceScatter(t2, ...)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x2 = tf.constant([8.,9.,10.,11.], shape=input_shape)

# Call model
y = m(x1, x2)