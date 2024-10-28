
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    t1 = tf.transpose(x1, perm=[1, 0])
    t2 = tf.transpose(x2, perm=[1, 0])
    
    # dot operation with transpose
    dot_product = tf.tensordot(t1, t2, axes=1)

    # convolution operation with transpose    
    conv = tf.nn.conv2d(t1, t2, strides=[1, 1, 1, 1], padding='SAME')
    
    return dot_product, conv

# Initializing the model
m = Model()

# Inputs to the model
input_shape1 = [2, 2]
input_shape2 = [2, 2, 1, 1]
x1 = tf.constant([[1., 2.], [3., 4.]], shape=input_shape1)
x2 = tf.constant([[1., 2.], [3., 4.]], shape=input_shape2)

# Call model
y1, y2 = m(x1, x2)