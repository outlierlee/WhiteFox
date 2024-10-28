
```python
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    self.lhs = tf.Variable([[2, 3], [5, 7]])
    self.rhs0 = tf.Variable([[1, 1], [2, 2]])
    self.rhs1 = tf.Variable([[3, 3], [4, 4]])

  def call(self, x):
    dot0 = tf.linalg.matmul(self.lhs, self.rhs0)
    dot1 = tf.linalg.matmul(self.lhs, self.rhs1)
    return dot0 + dot1

# Initializing the model
m = Model()

# Input
x = tf.constant([1.,2.,3.,4.], shape=[4])

# Call model
y = m(x)

# Now, y = DotMerger(lhs, rhs0, rhs1)
# where 
# DotMerger(lhs, rhs0, rhs1) = lhs * rhs0 + lhs * rhs1
```
Note: To trigger the `DotMerger` optimization pass, the model size should be less than or equal to the threshold size in the `DotMerger` pass. The threshold size can be adjustable using the `max_size_to_merge` attribute of the `DotMerger` pass. The exact attribute will be something like `-opt_threshold=16384` - it depends on the optimization library and configuration.
For the above model, take `max_size_to_merge = 16384` for example. Your model size should be less than or equal to `16384`, otherwise TensorFlow's `DotMerger` pass will skip your model.