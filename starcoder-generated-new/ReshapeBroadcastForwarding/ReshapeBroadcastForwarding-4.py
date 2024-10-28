
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    
  def call(self, x1):
    x2 = tf.broadcast_to(x1, [1])
    return tf.reshape(x2, [])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = []
x1 = tf.constant(5.)

# Call model
y = m(x1)
```

These models fulfill the specific requirements specified in the description and correctly apply the TensorFlow APIs needed in the problem specification.