
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.cast(x1, tf.float32)
    x3 = tf.cast(x2, tf.int32)
    return tf.cast(x3, tf.int32)


# Initializing the model
m = Model()

# Input to the model
x1 = tf.constant([4.5,5.6,6.7,7.8])

# Call model
y = m(x1)

# Print output
print(y) # Output will be [4, 5, 6, 7]