
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    sorted_tuple = tf.sort([x1, x1 * 2])
    return sorted_tuple[0] - sorted_tuple[1]

# Initializing the model
m = Model()

# Inputs to the model
x1 = tf.constant([4.,5.,6.,7.], shape=[4])

# Call model
y = m(x1)

print(y)