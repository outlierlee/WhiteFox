:
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  @tf.custom_gradient
  def custom_call(self, x):
    @tf.custom_gradient
    def grad(dy):
      return dy, None
  
    x = tf.raw_ops.Sharding(input=x)
    return x, grad