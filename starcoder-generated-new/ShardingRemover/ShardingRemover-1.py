
class MyModel(tf.Module):
  def __call__(self, x):
    y = tf.raw_ops.Sharding(input=x)
    return y
  
m = MyModel()
x = tf.constant([1.,2.,3.,4.])
y = m(x)

After running XLA, the IR should include a custom call instruction, whose operand is an input tensor, and the result tensor after the optimization should be the input tensor itself.