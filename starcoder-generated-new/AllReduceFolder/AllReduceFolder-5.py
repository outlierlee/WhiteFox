:
class Model(tf.distribute.StrategyScope):

  def __init__(self):
    super(Model, self).__init__()
    self.layernorm = tf.keras.layers.LayerNormalization(axis=None, reduction_axes=None)

  def call(self, x1, replica_context):
    x2 = self.layernorm(x1, training=False)
    return self.layernorm(x2, training=False, name=None)

