
```python
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def true_fn(self):
    return tf.constant(1)

  def false_fn(self):
    return tf.constant(0)

  def call(self, x1):
    result = tf.cond(tf.constant(True), self.true_fn, self.false_fn)
    return result

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
```