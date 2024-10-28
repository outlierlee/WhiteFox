
class Model(tf.keras.Model):
    
  def __init__(self):
    super(Model, self).__init__()
    self.dense1 = tf.keras.layers.Dense(1, dtype='float32')
    self.dense2 = tf.keras.layers.Dense(1, dtype='float32')

  def call(self, x1, x2):
    x3 = self.dense1(x1)    
    y1 = tf.cast(x3, 'int32')
    y2 = self.dense2(y1)
    return tf.cast(y2, 'float32')

# Initializing the model
m = Model()

# Inputs to the model
x1 = tf.constant([4.,5.,6.], shape=[3,])
x2 = tf.constant([1.,2.,3.], shape=[3,])

# Call model
y = m(x1, x2)
```