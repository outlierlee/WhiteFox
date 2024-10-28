
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, A):
    concatenated_tensor = tf.concat(A, axis=0)
    slice_start = sum([tf.size(element) for element in A])
    slice_size = concatenated_tensor.shape[0] - slice_start
    slice_output = tf.slice(concatenated_tensor, [slice_start], [slice_size])
    return slice_output

# Initializing the model
m = Model()

# Inputs to the model
A1 = tf.constant([4.,5.,6.,7.])
A2 = tf.constant([10.,11.,12.])

# Call model
y = m([A1, A2])