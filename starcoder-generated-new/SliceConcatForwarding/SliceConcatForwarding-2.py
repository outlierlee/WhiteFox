
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, A1, A2, start, size):
    output = tf.concat([A1, A2], axis=0)
    slice = tf.slice(output, start, size)
    return slice

# Initializing the model
m = Model()

# Inputs to the model
A1_shape = [2]
A2_shape = [3]
start = tf.constant([1])
size = tf.constant([3])
A1 = tf.constant([1., 2.], shape=A1_shape)
A2 = tf.constant([3., 4., 5.], shape=A2_shape)

# Call model
y = m(A1, A2, start, size)
print(y)

# Example output:
# tf.Tensor([2., 3., 4.], shape=(3,), dtype=float32)

