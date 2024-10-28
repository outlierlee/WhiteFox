
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    m1 = tf.Variable([[1, 2, 3], [4, 5, 6]], shape=(2, 3))
    m2 = tf.Variable([[7, 8], [9, 10], [11, 12]], shape=(3, 2))
    m3 = tf.Variable([[13, 14], [15, 16]], shape=(2, 2))
    return tf.linalg.matmul(x1, m1) + tf.linalg.matmul(x2, m2) + tf.linalg.matmul(x1, m3)


# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x2 = tf.constant([8.,9.,10.,11.], shape=input_shape)

# Call model
y = m(x1, x2)