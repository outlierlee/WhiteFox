
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.distribute.all_gather(x1, tf.distribute.HierarchicalCopyAllReduce(), axis=0)
    x3 = tf.distribute.all_gather(x2, tf.distribute.HierarchicalCopyAllReduce(), axis=0)
    return (x2, x3)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
# Note that the output will not be accessible without processing the output obtained directly
*y2, y3 = m(x1)
```