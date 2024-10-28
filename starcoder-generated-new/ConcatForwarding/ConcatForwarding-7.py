
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, A, B, C):
    axis = 0
    x1 = tf.concat([A, B], axis)
    return tf.concat([x1, C], axis)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2]
A = tf.constant([1.,2.,], shape=input_shape)
B = tf.constant([3.,4.,], shape=input_shape)
C = tf.constant([4.,5.,6.,7.], shape=[4])

# Call model
y = m(A, B, C)
```