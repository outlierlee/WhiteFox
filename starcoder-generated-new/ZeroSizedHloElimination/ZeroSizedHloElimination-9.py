
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    # here tf.reduce_sum(x) != x
    return tf.reshape(tf.reduce_sum(x), (0,))

# Initializing the model
m = Model()

# Creating dummy input with shape [1, 1]
x = tf.constant([[1.]], shape=[1, 1])

# Calling the model on the input
y = m(x)
```
This will trigger the ZeroSizedHloElimination optimization pass in TensorFlow XLA. The reshape operator will drop itself completely and the input will be safely removed, instead of producing an empty output.

The `tf.constant()` function in TensorFlow is a constant value operation, which cannot satisfy the zero-sized output requirements, thus it cannot trigger zero-sized cleanup, but we can use a dummy constant value `1.` instead to satisfy the side effect/operations/not a constant requirement.

Please note, XLA is enabled by default for TensorFlow. If you encounter an issue with this code that's why it is triggering optimization, you can disable XLA on a model-by-model basis using `tf.function(jit_compile=False)` before the first call to the model which should fix the issue.