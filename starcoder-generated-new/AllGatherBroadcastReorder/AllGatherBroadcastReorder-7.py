
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.broadcast_to(x1, [1, 2, 2])
    x3 = tf.all_gather(x2, tf.constant([0]))
    # x2:[batch, height, width], x3:[batch, num_replicas]
    return x3

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2, 2]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
```