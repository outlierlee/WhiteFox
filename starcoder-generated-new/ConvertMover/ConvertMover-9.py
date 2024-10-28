
class Model(tf.keras.Model):

  def __init__(self, higher_precision_dtype, lower_precision_dtype):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.cast(x1, higher_precision_dtype)
    x3 = tf.reduce_sum(x2, axis=0)
    x4 = tf.cast(x3, lower_precision_dtype)
    return x4

# Initializing the model
m = Model(tf.float16, tf.float32)

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)

