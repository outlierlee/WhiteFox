
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    i = tf.constant(0)
    c = lambda i: tf.less(i, 10)
    b = lambda i: tf.add(i, 1)
    r = tf.while_loop(c, b, [i])
    return x + r

# Initializing the model 
m = Model()

# Inputs to the model
input_shape = [1]
x = tf.constant([5], shape=input_shape)

# Call model
y = m(x)
```

# Note:

The model provided above, satisfies only Reshape requirement or triggering `WhileLoopTripCountAnnotator`. For deep learning models, complex mathematical computations are usually performed and hard to generate simple examples for purpose of triggering optimization passes like `WhileLoopTripCountAnnotator`. Deep learning model usually involve multiple layers of operations like `Conv2D`, `Dense`, etc. so those would not be easy to provide a simple example for `WhileLoopTripCountAnnotator`. Similarly, for triggering Optimization Pass "XLA Pipeline", a model with multiple complex operations would be required.