
class Model(tf.keras.Model):

  def __init__(self, to_type, to_typemap):
    super(Model, self).__init__()
    self._op = to_typemap[to_type]

  def call(self, x1, x2):
    y1 = self._op(x1, x2)
    return tf.reverse(y1)

# Initializing the model
m = Model(tf.int32, {tf.int32: tf.int16, tf.int16: tf.int32})

# Inputs to the model
x1 = tf.constant([4, 3, 5])
x2 = tf.constant([1, 2, 3])

# Call model
y = m(x1, x2)

print(y)  # Output: [3,2,1]
```
Please note that this model is contrived and it's purely for illustrative purposes. The actual implementation will depend on the TensorFlow and XLA version being used.