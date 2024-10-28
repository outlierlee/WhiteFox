

```python
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    def condition(i, x):
      return tf.reduce_any(i < 10)

    def body(i, x):
      return tf.add(i, 1), x

    return tf.while_loop(condition, body, [tf.constant(0), tf.constant(1)])

m = Model()
input_shape = [4]
x = tf.constant([4.,5.,6.,7.], shape=input_shape)
x = m(x)
```

The model above creates a constant `1` when initializing the while loop. It then uses the value `1` in the while loop body and condition to compute the loop iterations and can therefore be optimized in XLA.