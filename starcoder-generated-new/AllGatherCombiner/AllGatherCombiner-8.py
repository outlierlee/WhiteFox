

Create several AllGather operations with different tensors and the same all_gather_dimensions as follows:

```
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2, x3, all_gather_dim1, all_gather_dim2, all_gather_dim3):
    gather_1 = tf.distribute.experimental.AllGather(all_gather_dim=all_gather_dim1)
    gather_2 = tf.distribute.experimental.AllGather(all_gather_dim=all_gather_dim2)
    gather_3 = tf.distribute.experimental.AllGather(all_gather_dim=all_gather_dim3)
    
    result_1 = gather_1(x1)
    result_2 = gather_2(x2)
    result_3 = gather_3(x3)
    
    return result_1, result_2, result_3

# Initializing the model
m = Model()

# Inputs to the model
all_gather_dim1 = 0
all_gather_dim2 = 0
all_gather_dim3 = 0
x1 = tf.constant([1,2,3])
x2 = tf.constant([4,5,6])
x3 = tf.constant([7,8,9])

# Call model
result = m(x1, x2, x3, all_gather_dim1, all_gather_dim2, all_gather_dim3)

```
In this case, if the TensorFlow XLA compiler was capable of supporting the particular characteristics of this model (for example, it does not support AllGather with constrained layouts), you would expect the optimization pass `AllGatherCombiner` to be triggered.