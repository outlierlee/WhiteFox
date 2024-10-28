
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2, x3):
    t1 = tf.concat([x1, x2], 0)
    return tf.concat([t1, x3], 0)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2,2]
x1 = tf.constant([[4.,5.], [6.,7.]], shape=input_shape)
x2 = tf.constant([[1.,2.], [3.,4.]], shape=input_shape)
x3 = tf.constant([[8.,9.], [10.,11.]], shape=input_shape)

# Call model
y = m(x1, x2, x3)
```