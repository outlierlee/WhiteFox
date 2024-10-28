
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x, y):
    y = tf.cast(tf.reshape(y, [2, 1, 2, 3]), tf.float32)
    y = tf.cast(tf.reshape(y, [2, 2, 1, 3]), tf.float32)
    x = tf.cast(tf.reshape(x, [2, 1, 2, 3]), tf.float32)
    x = tf.cast(tf.reshape(x, [2, 2, 1, 3]), tf.float32)
    return tf.linalg.batch_matmul(x, y)

# Initializing the model
m = Model()

# Inputs to the model
x1 = tf.constant([[1, 2, 3], [4, 5, 6]])
y1 = tf.constant([[1, 4], [2, 5], [3, 6]])

# Call model
y = m(x1, y1)