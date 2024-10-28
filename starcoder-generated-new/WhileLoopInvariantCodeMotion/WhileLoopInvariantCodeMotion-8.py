
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    while_result = 0
    s1 = tf.constant(1)
    s2 = tf.constant(2)
    s3 = tf.constant(3)
    result = [s1, s2, s3]
    x1 = tf.constant(0)
    while_result = tf.concat([while_result, result[0] + s2], axis=0)
    while_result = tf.concat([while_result, result[1] + s3], axis=0)
    while_result = tf.concat([while_result, result[2] + s1], axis=0)
    return while_result

# Initializing the model
m = Model()

# Inputs to the model
x1 = tf.constant([4,5,6,7])

# Call model
y = m(x1)