

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, a1, a2):
    a3 = tf.concat([a1, a2], axis=0)
    return tf.slice(a3, [3], [2])

# Initializing the model
m = Model()

# Inputs to the model
a1 = tf.constant([1., 2., 3., 4., 5., 6.], shape=[3,2])
a2 = tf.constant([1., 2.], shape=[2])

# Call model
y = m(a1, a2)

The model here is a 2D array and the slice start is at 4. So the slice size is 2 (slice size = slice limit - slice start), which satisfy the constraints.