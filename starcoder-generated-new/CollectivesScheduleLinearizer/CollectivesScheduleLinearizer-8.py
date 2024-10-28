
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    self.strategy = tf.distribute.MirroredStrategy()
    self.collective_ops = [tf.distribute.Reduce, tf.distribute.AllReduce, tf.distribute.CollectivePermuteStart, tf.distribute.AsyncStart, tf.distribute.AllGather]

  def call(self, x1):
    scope = tf.distribute.experimental.CollectiveCommunication.ALL
    x2 = self.strategy.run(lambda: tf.distribute.AllReduce(x1, oper=tf.distribute.ReduceOp.MEAN, communication=tf.distribute.experimental.CollectiveCommunication.AUTO, options=None, group_assignment=None, auto_thresholds=None, name='all_reduce'))
    x3 = tf.Print(x2,  [x2], 'tensor after reduction: ', summarize=1000)
    x4 = self.strategy.run(lambda: tf.distribute.AllGather(x3, group_assignment=None, auto_thresholds=None, name='all_gather'))
    return tf.Print(x4, [x4], 'tensor after allgather: ', summarize=1000)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)