
class Model(tf.keras.Model):

  def __init__(self, r0, r1):
    super(Model, self).__init__()
    self.r0 = r0
    self.r1 = r1

  def call(self, x1):
    t1 = tf.raw_ops.AllReduce(operations=["MAX"], values=[x1.numpy()], group_size=self.r0, group_count=1, xla_global_device="")
    t2 = tf.raw_ops.AllReduce(operations=["MAX"], values=[t1.numpy()], group_size=self.r1, group_count=1, xla_global_device="")
    return t2

# Initializing the model
r0 = 2
r1 = 4
m = Model(r0, r1)

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
```