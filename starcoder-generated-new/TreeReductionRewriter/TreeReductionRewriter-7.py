
class Model(tf.keras.Model):

  def __init__(self, threshold):
    super(Model, self).__init__()
    self.threshold = threshold

  def call(self, x):
    x_shape = x.shape
    reduced_dims = [idx for idx in range(len(x_shape)) if x_shape[idx] > self.threshold]
    reduce_op = getattr(tf, f"reduce_sum")
    return reduce_op(x, axis=reduced_dims)


# Initializing the model
m = Model(threshold=1000)

# Inputs to the model
input_shape = [1001,1,1]
x1 = tf.random.normal(shape=input_shape)

# Call model
y = m(x1)
```
Please provide a TensorFlow model solution for the problem outlined.