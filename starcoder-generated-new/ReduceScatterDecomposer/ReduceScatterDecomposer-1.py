
class MyModel(tf.keras.Model):

  def __init__(self):
    super(MyModel, self).__init__()

  def call(self, x):
    hlo_context = tf.xla.experimental.distribute_strategy.HloDistributionStrategyContext()
    inputs = hlo_context.xla_compile(MyModel.call, args=[x])
    return tf.xla.experimental.reduce_scatter(inputs, x.shape, axis=0, type=x.dtype)


# Initializing the model
m = MyModel()

# Inputs to the model
input_shape = [4]
x = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x)