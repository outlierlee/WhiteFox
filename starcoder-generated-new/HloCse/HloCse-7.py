
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    y = tf.constant([6, 7, 8, 9, 10])

    # Identical instructions
    z1 = tf.add(x, y)
    _ = tf.squared_difference(z1, z1)    # Side effect instruction
    z2 = tf.add(x, y)
    _ = tf.multiply(z1, z2)               # Side effect instruction 
    z3 = tf.add(x, y)

    # Identical constants
    c1 = tf.constant([1, 2, 3, 4, 5])
    c2 = tf.constant([1, 2, 3, 4, 5])

    # Identical iota instructions
    i1 = tf.raw_ops.Iota(range=tf.constant([5]), name=None)
    i2 = tf.raw_ops.Iota(range=tf.constant([5]), name=None)

    return z1, z2, z3, c1, c2, i1, i2

# Initializing the model
m = Model()

# Inputs to the model
x = tf.constant([1, 2, 3, 4, 5])

# Call model
z1, z2, z3, c1, c2, i1, i2 = m(x)
print(z1, z2, z3, c1, c2, i1, i2)