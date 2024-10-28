
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.raw_ops.AllReduce(tensor=x1, group_key=b'', instruction='Add')
    return tf.raw_ops.AllReduce(tensor=x2, group_key=b'', instruction='Add')

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2,2]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
```
