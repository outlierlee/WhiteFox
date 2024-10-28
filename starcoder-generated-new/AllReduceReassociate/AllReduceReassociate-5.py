
Class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    x3 = tf.reduce_mean(x1)
    x4 = tf.reduce_mean(x2)
    return x3 + x4

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2,2]
x1 = tf.constant([1.,2.,3.,4.], shape=input_shape)
x2 = tf.constant([5.,6.,7.,8.], shape=input_shape)

# Call model
y = m(x1, x2)
```