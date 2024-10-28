:
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x, y):
    eliminate_type = tf.float32
    replace_with_type = tf.int32
    x = tf.cast(x, eliminate_type)
    y = tf.cast(y, eliminate_type)
    result = tf.add(x, y, name=None)
    result = tf.cast(result, replace_with_type)
    return result

# Initializing the model
m = Model()

# Inputs to the model
x = tf.constant([4, 5, 6], shape=[3], dtype=tf.int32)
y = tf.constant([1, 2, 3], shape=[3], dtype=tf.int32)

# Call model
z = m(x, y)