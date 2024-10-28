
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    sharding = tf.raw_ops.Sharding(input=x)
    return sharding

# Initializing the model
m = Model()
x = tf.constant([4.,5.,6.,7.], shape=[4])

# Call model
y = m(x)


