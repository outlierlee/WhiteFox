
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2, x3):
    y1 = tf.raw_ops.ReduceScatter(input=x1, reduction_op='add', ...)
    y2 = tf.raw_ops.ReduceScatter(input=x2, reduction_op='add', ...)
    y3 = tf.raw_ops.ReduceScatter(input=x3, reduction_op='add', ...)

    return y1, y2, y3

# Initializing the model
m = Model()

# Inputs to the model
x1 = ...
x2 = ...
x3 = ...

# Call model
y1, y2, y3 = m(x1, x2, x3)
```

Please specify your model and let TensorFlow XLA optimize it through the `ReduceScatterCombiner` optimization pass.