
class Model(tf.keras.Model):

  def __init__(self, concatted_sizes, start, size):
    super(Model, self).__init__()
    self.concatted_sizes = concatted_sizes
    self.start = start
    self.size = size

  def call(self, *inputs):
    concat_tensor = tf.concat(inputs, axis=0)
    slice_tensor = tf.slice(concat_tensor, 
                           [self.concatted_sizes[0] + self.concatted_sizes[1] - self.start - self.size], 
                           [self.size])
    return slice_tensor

# Initializing the model
m = Model([4,2], 2, 2)

# Inputs to the model
x1 = tf.constant([4.,5.,6.,7.])
x2 = tf.constant([8.,9.,10.,11.])

# Call model
y = m(x1, x2)
```