
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

    self.pad = tf.keras.layers.ZeroPadding2D((1, 1))
    self.relu = tf.keras.layers.ReLU()

  def call(self, x):
    t1 = tf.convert_to_tensor(tf.raw_ops.FakeQuantWithMinMaxVars(x, min=-1, max=1, num_bits=8, narrow_range=False), dtype=tf.float32)
    t2 = self.pad(t1)
    return self.relu(t2)


# Model initialization and call
m = Model()
input_shape = [100, 100, 3]
x = tf.ones(input_shape, dtype=tf.float16)
m(x)