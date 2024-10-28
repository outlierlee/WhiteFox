
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    self.b = tf.Variable(1.0, shape=[4, 4])

  def call(self, x):
    # operations with at least one operand constant, 
    # and the other operand is a broadcast of constant
    c = x * self.b
    scream = self.scream()   # here is the constant folding
    return tf.math.add(x, c)

  def scream(self):
    return 42    # here is the constant operation

# Initializing the model
m = Model()

# Inputs to the model
x = tf.constant([1.,2.,3.,4.], shape=[4])

# Call model
y = m(x)