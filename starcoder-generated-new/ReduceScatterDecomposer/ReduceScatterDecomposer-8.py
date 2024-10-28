
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    input_placeholder = tf.placeholder(tf.float32, shape=(None,100))
    reduced_scatter = tf.xla.experimental.reduce_scatter(input_placeholder, np.array([0,1,0]), 'sum')
    return reduced_scatter

# Initializing the model
m = Model()
m.build(input_shape=(None,100))

# Inputs to the model
x1 = tf.constant([4.,5.,6.,7.], shape=(2,2))

# Call model
y = m(x1)
```
Make sure `tf.xla.experimental.reduce_scatter` only resides in your model in place of `tf.placeholder`, as `tf.placeholder` is not officially supported in version newer than TensorFlow 2.5 and is not in TensorFlowXLA's whitelist for interpreting.