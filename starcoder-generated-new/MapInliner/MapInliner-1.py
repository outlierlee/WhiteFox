
class MyModel(tf.keras.Model):

  def __init__(self):
    super(MyModel, self).__init__()

  def call(self, x):
    def map_function(y):
      return tf.math.square(y)
    return tf.map_fn(map_function, x)

# Initializing the model
m = MyModel()

# Inputs to the model
input_shape = [4]
input_tensor = tf.constant([1.,2.,3.,4.], shape=input_shape)

# Test model
print(m(input_tensor))