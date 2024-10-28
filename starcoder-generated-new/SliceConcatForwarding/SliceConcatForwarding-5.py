
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    t1 = tf.concat([x1, x2], axis=0)
    return tf.slice(t1, [tf.size(x1)], [tf.size(x2)])

# Initializing the model
m = Model()

# Inputs to the model
input_shape1 = [2]
input_shape2 = [3]
x1 = tf.constant([4.,5.], shape=input_shape1)
x2 = tf.constant([6.,7.,8.], shape=input_shape2)

# Call model
y = m(x1, x2)