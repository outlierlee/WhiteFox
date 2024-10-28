
class Model(tf.keras.Model):

  def __init__(self, start_indices, slice_sizes, update):
    super(Model, self).__init__()
    self.start_indices = start_indices
    self.slice_sizes = slice_sizes
    self.update = update

  def call(self, x1):
    x2 = tf.dynamic_update_slice(x1, self.update, self.start_indices)
    return tf.dynamic_slice(x2, self.start_indices, self.slice_sizes)

# Initializing the model
m = Model([1,0], [2,2], [[0.,1.],[2.,3.]])

# Inputs to the model
input_shape = [4,4]
x1 = tf.constant([[1.,2.,3.,4.],[10.,11.,12.,13.],[20.,21.,22.,23.],[30.,31.,32.,33.]], shape=input_shape)

# Call model
y = m(x1)
```