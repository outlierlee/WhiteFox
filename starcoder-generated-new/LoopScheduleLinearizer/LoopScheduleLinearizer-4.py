
```python
class Model(tf.keras.Model):
  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    def loop_body(i, x):
      # read operation
      read = tf.gather(x, i)
      # write operation
      write = tf.tensor_scatter_nd_update(x, [[i]], [read])
      return [i + 1, write]

    _, result = tf.while_loop(lambda i, x: i < 2, loop_body, [0, x], shape_invariants=[tf.TensorShape([]), tf.TensorShape([None])])
    return result

# Initializing the model
m = Model()

# Inputs to the model
x = tf.constant([1,2,3,4])

# Call model
y = m(x)
```