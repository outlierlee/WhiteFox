
The following is a simple model that satisfies the requirements:

```python
# Assuming that we have a "combine_threshold_in_bytes" (let's say 2, in this case) and a "combine_threshold_count" (let's say 2, in this case)

# Define a simple model class
class Model(tf.keras.Model):
    def __init__(self):
        super(Model, self).__init__()
        self.r1 = tf.math.reduce_sum([0,1])
        self.r2 = tf.math.reduce_sum([2,3])

        self.rs1 = tf.raw_ops.ReduceScatter(input=self.r1, reduction_op='add', instance_dims=1, axis=0)
        self.rs2 = tf.raw_ops.ReduceScatter(input=self.r2, reduction_op='add', instance_dims=1, axis=0)
  
    def call(self, x):
        self.rs1 = x
        self.rs2 = x 
```

Note: The model may not work as expected if respecting optimum values for `combine_threshold_in_bytes` and `combine_threshold_count` is not guaranteed.