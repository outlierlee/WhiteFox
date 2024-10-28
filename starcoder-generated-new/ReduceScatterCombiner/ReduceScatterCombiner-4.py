
```python
class Model(tf.keras.Model):
  def __init__(self, num_inputs):
    super(Model, self).__init__()
    self.num_inputs = num_inputs
    self.inputs = [tf.Variable(tf.random.normal([10])) for _ in range(num_inputs)]
    self.reduce_scatters = [tf.raw_ops.ReduceScatter(
        input=input_, reduction_op='add', scatter_dims=0)
                             for input_ in self.inputs]    

  def call(self):
    return sum(self.reduce_scatters)

num_inputs = tf.constant(21, dtype=tf.int32)

model = Model(num_inputs)

y = model()
```
The implemented model architecture is a model with `num_inputs` number of `tf.raw_ops.ReduceScatter` operations which adds the elements for a given dimension in a computation. As per the conditions mentioned above, the total size of the tensors in operation inputs should be greater than `combine_threshold_in_bytes` and the number of operations should be more than `combine_threshold_count`. This model has a number of `ReduceScatter` operations which satisfy all the conditions, to test with different combinations please adjust the conditions or change the number of `ReduceScatter` operations.