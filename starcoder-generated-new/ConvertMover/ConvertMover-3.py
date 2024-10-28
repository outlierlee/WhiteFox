
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    t1 = tf.cast(x1, dtype=tf.float64)
    t2 = tf.cast(x1 + tf.constant([0.5]), dtype=tf.float32)
    t3 = tf.where(t1>0.0, -t1, tf.zeros([4], dtype=tf.complex64))
    return tf.cast(t3, dtype=tf.float32)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([1.5,2.5,3.5,4.5], shape=input_shape)

# Call model
y = m(x1)
```