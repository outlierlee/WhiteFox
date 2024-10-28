

```python
import tensorflow as tf

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    shape_tensor = tf.shape(input=x)

    def if_true():
      return shape_tensor[0]

    def if_false():
      return shape_tensor[1]

    return tf.cond(tf.constant(True), if_true, if_false)

# Initializing the model
m = Model()

# Inputs to the model
x = tf.constant([[1, 2, 3], [4, 5, 6]])

# Call model
y = m(x)
```

Note: even though this example does not trigger the `ConditionalCanonicalizer` optimization pass, understanding how `tf.cond` operates in TensorFlow is essential for understanding the behavior and the potential optimizations TensorFlow XLA may apply.