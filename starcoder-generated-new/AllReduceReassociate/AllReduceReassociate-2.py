

Assuming we have the following two input tensors:
```
x1 = tf.constant([4.,5.,6.,7.], shape=[4])
x2 = tf.constant([1.,2.,3.,4.], shape=[4])
```

Please design a model that satisfies the above mentioned requirements.

# Model

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    x1 = tf.reduce_sum(x1, axis=0)
    x2 = tf.reduce_sum(x2, axis=0)
    x3 = x1 * x2
    return x3

# Initializing the model
m = Model()

# Inputs to the model
x1 = tf.constant([4.,5.,6.,7.], shape=[4])
x2 = tf.constant([1.,2.,3.,4.], shape=[4])

# Call model
y = m(x1, x2)