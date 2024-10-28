
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x1 = tf.cast(x1, tf.float32)
    x1 = tf.cast(x1, tf.int32)
    return tf.cast(x1, tf.float32)