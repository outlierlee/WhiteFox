
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2, x3):
    t1 = tf.reduce_sum(x1)
    t2 = tf.reduce_sum(x2)
    t3 = tf.reduce_sum(x3)
    combined = t1 + t2 + t3
    return combined

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([1,1,1,4], shape=input_shape)
x2 = tf.constant([2,1,0,2], shape=input_shape)
x3 = tf.constant([3,1,0,1], shape=input_shape)

# Call model
y = m(x1, x2, x3)
```