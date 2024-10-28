
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.raw_ops.AllReduce(input=x1, group="0:1,")
    x3 = tf.raw_ops.AllReduce(input=x2, group="0:1,")
    return tf.raw_ops.AllReduce(input=x3, group="0:1,")

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
```