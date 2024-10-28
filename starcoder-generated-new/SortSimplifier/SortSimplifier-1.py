
class MyModel(tf.keras.Model):

  def __init__(self):
    super(MyModel, self).__init__()

  def call(self, x):
    sorted_x, unused_x = tf.sort(x, num_or_size_splits=2)
    return sorted_x

# Initializing the model
m = MyModel()

# Inputs to the model
x = (tf.constant([2, 1]), tf.constant([2, 1, 3]))

# Call model
output = m(x)

```
This `MyModel` will not be optimized due to the unused sort output.

