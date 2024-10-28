
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    x1_t = tf.transpose(x1, perm=[1, 0])
    x2_t = tf.transpose(x2, perm=[1, 0])
    dot_product = tf.tensordot(x1_t, x2_t, axes=1)
    return dot_product