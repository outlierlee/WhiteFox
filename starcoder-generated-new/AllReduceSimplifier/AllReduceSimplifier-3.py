
```
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    t1 = tf.distribute.all_gather(x, axis=0)
    t2 = tf.distribute.experimental.reducescatter(t1, reduction='sum')
    t3 = tf.distribute.experimental.all_reduce(t2, reduction='sum')
    return tf.distribute.experimental.all_reduce(t3, reduction='minimum')

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x)
```
Please note that `tf.distribute.experimental.all_reduce` and `tf.distribute.experimental.reduce_scatter` APIs are experimental and subject to changes.