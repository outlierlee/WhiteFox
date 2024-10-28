
class Model(tf.keras.Model):

  def __init__(self, num_devices, num_repeats):
    super(Model, self).__init__()
    self.num_devices = num_devices
    self.num_repeats = num_repeats

  def call(self, x):
    x = tf.split(x, self.num_repeats, axis=-1)
    for i in range(self.num_devices):
        
      x[i] = tf.experimental.numpy.reshape(x[i], (1 , 1 , 8 , 8 , 8))
    reduced_scatter = tf.experimental.xla.reduce_scatter(x, {
  'TOKEN': tf.constant(-1)})
    return reduced_scatter

num_devices = 4
num_repeats = 2
m = Model(num_devices, num_repeats)
x = tf.constant([(1, 2), (3, 4)], shape=(num_devices*num_repeats,))
y = m(x)
print(y)