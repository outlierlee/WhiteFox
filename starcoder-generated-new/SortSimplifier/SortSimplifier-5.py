:
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    input = (x1, tf.ones([2]), tf.zeros([3]))
    sorted_tuple = tf.sort(input)
    used_operation = tf.reduce_sum(sorted_tuple[0])
    return used_operation