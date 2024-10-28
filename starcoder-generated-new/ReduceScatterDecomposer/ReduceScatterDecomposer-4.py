
```python
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    reduced_scatter = tf.xla.experimental.reduce_scatter(x1, [[0,1]])
    return reduced_scatter

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2,2]
x1 = tf.constant([[1.,2.], [3.,4.]], shape=input_shape)

# Call model
y = m(x1)
```