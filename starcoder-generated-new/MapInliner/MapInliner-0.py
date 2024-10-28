
class Model(tf.keras.Model):
    
  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    def func(x):
        return tf.math.abs(x)

    return tf.map_fn(func, x)

# Initializing the model
model = Model()

# Inputs to the model
input_shape = [2]
x = tf.constant([-1,-2], shape=input_shape)

# Call model
y = model(x)
```