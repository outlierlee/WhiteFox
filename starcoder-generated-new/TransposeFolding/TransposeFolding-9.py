

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    x1 = tf.transpose(x1, perm=[1, 0])
    x2 = tf.transpose(x1, perm=[1, 0])
    dot_product = tf.tensordot(x1, x2, axes=1)
    conv = tf.nn.conv2d(x1, x2, strides=[1, 1, 1, 1], padding='SAME')
    return dot_product, conv

# Initializing the model
m = Model()

# Inputs to the model
input_shape1 = [4,2]
input_shape2 = [4,4]
x1 = tf.constant([1,2,3,4,5,6,7,8], shape=input_shape1)
x2 = tf.constant([1,2,3,4,5,6,7,8], shape=input_shape2)

# Call model
y1, y2 = m(x1, x2)

