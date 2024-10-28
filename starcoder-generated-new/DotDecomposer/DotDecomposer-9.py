

class DotNonCanonicalModel(tf.keras.Model):

  def __init__(self):
    super(TypeModel, self).__init__()

  def call(self, x, y):
    # Non-canonical dot operation
    return tf.tensordot(x, y, axes=[[1, 2], [0, 1]])

# Initializing the model
m = DotNonCanonicalModel()

# Inputs
x = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
y = tf.constant([1, 2, 3, 4])

# Call model
z = m(x, y)

```