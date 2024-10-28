
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    x3 = tf.slice(x1, [1], [3])
    x4 = tf.slice(x2, [1], [3])
    x5 = tf.math.add(x3, x4)
    return x5

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x2 = tf.constant([1.,2.,3.,4.], shape=input_shape)

# Call model
y = m(x1, x2)
```

Our model satisfies conditions:

1. All operands of the elementwise operation are slices.
2. All slices are from the same indices of slice sources with compatible shapes.
3. The elementwise operation and its operands have not been transformed before (their user count is not 0).
4. The elementwise operation and its operands have the same opcode and result element type.
5. The accumulated size of the group of operations is not less than the size of such a bigger tensor. This is a heuristic to ensure that the transformation does not cause us to do more elementwise operations.

Therefore, our model can be used as the input to trigger the optimization pass `SliceSinker` in TensorFlow XLA.