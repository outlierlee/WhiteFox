

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    # AllGather operation
    t1 = tf.distribute.all_gather(x1, axis=0)
    # ReduceScatter operation
    t2 = tf.distribute.experimental.reducescatter(t1, reduction='sum')
    # AllReduce operation
    t3 = tf.distribute.experimental.all_reduce(t1, reduction='sum')
    # AllReduce operation
    return tf.distribute.experimental.all_reduce(x1, reduction='sum')


# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
```