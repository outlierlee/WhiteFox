
class Model(tf.keras.Model):
    
  def __init__(self):
    super(Model, self).__init__()
    self.reduce_scatter_1 = tf.raw_ops.ReduceScatter(input_tensor1, axis=1, method='sum', n=2)
    self.reduce_scatter_2 = tf.raw_ops.ReduceScatter(input_tensor2, axis=1, method='add', n=2)
  
  def call(self, inputs):
    summed_results = tf.add(self.reduce_scatter_1, self.reduce_scatter_2)
    result = tf.reduce_sum(summed_results)
    return result

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([1,2,3,4], shape=input_shape)
x2 = tf.constant([5,6,7,8], shape=input_shape)

# Call model
y = m([x1, x2])
```
The constraint of having only one user for `ReduceScatter` operations is intended to ensure the model is amenable to optimization with XLA, as this optimization pass only works for patterns where intermediate tensors are produced as output by one single operation. If complex transformations are required, the existing pattern compliance checks might reject the model, although other optimization passes might still converge to the output. It is worth noting that optimized models might follow different patterns to meet advanced optimization targets, so these models are verified only based on a single transform.