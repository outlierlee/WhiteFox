:

```python
class Model(tf.keras.Model):
  def __init__(self):
    super(Model, self).__init__()

  def call(self, x, n=50):
    return tf.while_loop(
        cond=lambda i, loop_vars: i < n,
        body=lambda i, loop_vars: [i+1, tf.add(loop_vars[0], tf.constant(5))],
        loop_vars=[tf.constant(0), x]
    )[1]

# Initializing the model
m = Model()

# Inputs to the model
n, x = 50, tf.constant(0)

# Call model
y = m(x, n)
```
Please provide one such model.