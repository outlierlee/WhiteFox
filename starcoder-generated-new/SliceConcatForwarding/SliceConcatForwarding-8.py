

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    input_shape = x.shape
    slice_start = x.shape[0] - x.shape[1]
    x = self.forwarding(x)
    sliced_x = tf.slice(x, [slice_start], [input_shape[1]])
    return sliced_x

  def forwarding(self, x):
    reconcat_indices = np.cumsum(np.array([x.shape[1], x.shape[2]]))
    x = tf.concat([x[:reconcat_indices[0]], x[reconcat_indices[0]:reconcat_indices[1]]], axis=1, name="ConcatOperator")
    return x


# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4, 2]
x = tf.constant([1,2,3,4,5,6,7,8], shape=input_shape, name="Input")

# Call model
y = m(x)

Call model
y = m(x)
```