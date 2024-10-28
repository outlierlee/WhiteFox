
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    y1 = tf.slice(x1, [0,0], [2,2])
    y2 = tf.slice(x2, [0,0], [2,2])
    return tf.math.multiply(y1, y2)

# Initializing the model
m = Model()

# Inputs to the model
input_shape1 = [4,4]
input_shape2 = [4,4]
x1 = tf.constant([4.,5.,6.,7.,8.,5.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.], shape=input_shape1)
x2 = tf.constant([1.,2.,5.,4.,1.,3.,5.,6.,2.,8.,7.,9.,3.,7.,8.,11.], shape=input_shape2)

# Call model
y = m(x1, x2)

I have no idea how to write test code to exercise these patterns for optimization. Please help.