

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    tf.device('/cpu:0')
    i = tf.constant(0, dtype=tf.int32)
    conditions = lambda i: tf.less(i, tf.constant(10))
    body = lambda i: tf.add(i, 1)
    r = tf.while_loop(conditions, body, [i])
    return tf.reshape(r, [10])


m = Model()
input_shape = [10]
x1 = tf.constant([1.,2.,3.,4.,5.,6.,7.,8.,9.,10.], shape=input_shape)
y = m(x1)