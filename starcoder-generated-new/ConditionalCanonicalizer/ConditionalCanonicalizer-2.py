
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    def true_fn():
      return tf.constant(1)

    def false_fn():
      return tf.constant(0)

    result = tf.cond(tf.constant(True), true_fn, false_fn)
    return result

# Initializing the model
m = Model()

# Inputs to the model
x = tf.constant(1)

# Call model
y = m(x)
```

In this model, the `tf.cond` operation is used to select either the tensor with constant value 1 or the tensor with constant value 0, regardless of input. As the model output is not a tuple, the `ConditionalCanonicalizer` will be triggered.