
class Model(tf.Module):

  def __call__(self, x):
    x_reshape = tf.reshape(x, [4, 2])
    x_broadcast = tf.broadcast_to(x_reshape, [2, 4, 2])
    return tf.raw_ops.Sharding(input=x_broadcast)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x = tf.constant([1.,2.,3.,4.], shape=input_shape)

# Call model
y = m(x)

# If model execution is done, you will get result where sharding instruction is removed and operand is directly returned, following ShardingRemover transformation pass.