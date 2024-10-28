
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, a1, a2, s1, s2):
    x = tf.concat([a1, a2], axis=1)
    start = s1 - tf.math.reduce_sum(tf.shape(a1))
    return tf.slice(x, [start], [tf.shape(x)[0] - start])

# Initializing the model
m = Model()

# Inputs to the model
a1 = tf.constant([1., 2., 3., 4.], shape=[4])
a2 = tf.constant([5., 6., 7., 8.], shape=[4])
s1= tf.constant([7.])
s2 = tf.constant([10.])

# Call model
y = m(a1, a2, s1, s2)