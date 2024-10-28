

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    x1 = tf.reduce_mean(x1, axis=1)
    x2 = tf.reduce_sum(x2, axis=1)
    x_final = tf.math.add(x1, x2)
    return x_final

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4,2]
x1 = tf.constant([2.,5.,1.,4.], shape=input_shape)
x2 = tf.constant([3.,6.,7.,8.], shape=input_shape)

# Call model
y = m(x1, x2)
```
Note: All doctests and examples should be clear and self-explanatory. They should be produced with TensorFlow 2.0 or higher.