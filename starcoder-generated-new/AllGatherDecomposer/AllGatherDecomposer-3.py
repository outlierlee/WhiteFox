
```
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    return tf.distribute.reduce(tf.distribute.get_replica_context().all_reduce_handle(), x, tf.distribute.reduce_op.SUM)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2,2]
x = tf.constant([2.,4.,6.,8.], shape=input_shape)

# Convert tensors to distribute strategy
x = m.experimental_distribute_datasets(x)

# Call model
y = m(x)
```

In this model, `call()` method has a `tf.distribute.get_replica_context().all_reduce_handle()`. `all_reduce_handle()` is used as the handle to communicate in a reduce-scatter operation. It sends and receive values to all replicas. Hence, `AllGatherDecomposer` should trigger on this model. Please note that, you will need to run this code under the TensorFlow Distributed Strategy Scope, and you have to ensure the configuration of the runtime is correct in order to trigger the `AllGatherDecomposer` optimization because whether the runtime environment is correct can depend on the `should_decompose_` function definition.