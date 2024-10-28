

class Model(tf.keras.Model):
  def __init__(self):
    super(Model, self).__init__()

  def call(self, A, B, C, axis):
    t1 = tf.concat([A, B], axis)
    return tf.concat([t1, C], axis)

# Initializing the model
m = Model()

# Inputs to the model
A = tf.constant([1.,2.,3.,4.], shape=[4])
B = tf.constant([5.,6.,7.,8.], shape=[4])
C = tf.constant([9.,10.,11.,12.], shape=[4])
axis = 0

# Call model
y = m(A, B, C, axis)
```