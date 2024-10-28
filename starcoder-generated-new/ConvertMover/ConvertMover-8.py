

Create a model that defines these requirements.

# Solution
```python
class Model(tf.keras.Model):

  def __init__(self, higher_precision_dtype=tf.float32, lower_precision_dtype=tf.bfloat16):
    super(Model, self).__init__()
    self.convert = tf.cast
    self.op1 = tf.reduce_sum
    self.op2 = tf.reshape
    self.convert_to_upper = tf.cast

  def call(self, x1):
    x2 = self.op1(x1, axis=-1)
    x3 = self.convert(x2, self.convert_to_upper)
    x4 = self.op2(x3, x2.shape)
    return x4

m = Model()
x1 = tf.constant([1,2,3,4], shape=(4), dtype=tf.int32)
y = m(x1)
```