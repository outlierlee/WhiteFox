
class MyModel(tf.keras.Model):

  def __init__(self):
    super(MyModel, self).__init__()

  def call(self, x1):
    strategy = tf.distribute.experimental.CollectiveAllReduceStrategy()
    all_reduce_scope = strategy.scope()
    
    with all_reduce_scope:
      x2 = tf.distribute.strategy_utils.get_collective_permute_token()
      token = tf.distribute.CollectivePermuteToken(x2)

      reduce = tf.distribute.AllReduce(replica_id=0, app_name="AllReduceTest", token=token, **{'ReductionString': 'MIN'})
      reduce.postbody = tf.function(reduce.postbody).call
      reduce(x1)

      gather = tf.distribute.AllGather(replica_id=0, app_name="AllGatherTest", token=token)
      gather(x1)

      return True

# Initializing the model
m = MyModel()

# Inputs to the model
input_shape = [2,2]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)