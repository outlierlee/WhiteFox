

The given pattern can be written in a TensorFlow model like this:

```python
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    i = tf.constant(0)
    def body(i):
      return tf.add(i, 1)
    def cond(i):
      return tf.less(i, 10)
    r = tf.while_loop(cond, body, [i])
    return r

m = Model()
input_shape = [1]
x = tf.constant([0], shape=input_shape)
y = m(x)
```
The model contains a While loop with a body `tf.add(i, 1)`, continuing until the condition `tf.less(i, 10)` is no longer satisfied. The returned value `r` of the model will be 10 as the while loop executes for 10 iterations.