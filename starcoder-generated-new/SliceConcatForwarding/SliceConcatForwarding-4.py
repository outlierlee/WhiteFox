
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    
  def call(self, x1, x2, x3):
    t1 = tf.concat([x1, x2, x3], axis=0)
    return tf.slice(t1, [0], [t1.shape[0]])

# Initializing the model
m = Model()

# Inputs to the model
x1 = tf.constant([4.,5.,6.,7.], shape=[4])
x2 = tf.constant([4.,5.,6.,7.], shape=[4])
x3 = tf.constant([4.,5.,6.,7.], shape=[4])

# Call model
y = m(x1, x2, x3)
```

Please ensure your code is providing equivalent outputs to the TensorFlow examples.