
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    strategy = tf.distribute.experimental.CentralStorageStratagy()
    reduce_value = tf.function(lambda x:
                               tf.distribute.AllReduce(x, 'SUM', strategy=strategy))()
    value_per_device = reduce_value(x1)
    gathered_value = tf.function(lambda x:
                                  tf.distribute.AllGather(x, strategy=strategy))()
    return gathered_value(value_per_device)

m = Model()
input_shape = [2]
x_value = tf.constant([1.]*2, shape=input_shape)
y = m(x_value)

