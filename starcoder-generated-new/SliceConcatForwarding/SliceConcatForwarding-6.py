
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  # t3 is assumed to be the tensor that can be forwarded from the main model
  def call(self, x1, x2, x3):
    t1 = tf.concat([x1, x2, x3], axis=0)
    t2 = tf.slice(t1, [x2.shape[0]+x3.shape[0]], [x1.shape[0]])
    return t2

# Initializing the model
m = Model()

# Inputs to the model
input_shape1 = [2]
input_shape2 = [3]
input_shape3 = [2]
x1 = tf.constant([2.,4.], shape=input_shape1)
x2 = tf.constant([1.,2.,3.], shape=input_shape2)
x3 = tf.constant([4.,5.], shape=input_shape3)

# Call model
y = m(x1, x2, x3) # forwarding x1 based on x2, x3 by slicing from x2+x3 in x1.