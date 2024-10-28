
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    return tf.xla.experimental.reduce_scatter(x1)

# Initializing the model
m = Model()


# Inputs to the model. 
input_shape = [2, 2] # Tensor is shaped [2, 2] on each device, so total shape is [4, 2]
x1 = tf.constant([[4., 5.], [6., 7.]], shape=input_shape)

# Call model
y = m(x1)
```  
This example above is not a perfect match as TensorFlow gives error for the current setup. Distributed training even with all-reduce operations may not be feasible when running in a single machine. However, understanding the XLA decomposition structure is a good exercise in understanding the underlying implementation of TensorFlow's XLA (e.x. reduce-scatter vs broadcast).