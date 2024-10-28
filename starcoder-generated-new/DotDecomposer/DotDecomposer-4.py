
```python
class Model(tf.keras.Model):
  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    y = tf.transpose(x, perm=[1, 0, 2])
    z = tf.tensordot(x, y, axes=[[0, 2], [0, 2]])
    return z

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2, 2, 2]
x = tf.constant([[1., 2.], [3., 4.]], shape=input_shape)

# Call model
z = m(x)
```

If you run `tf.xla.experimental.compile(m, inputs=[x])`, `DotDecomposer` optimization pass will be triggered and the `tensordot` operation will be converted into a canonical form.