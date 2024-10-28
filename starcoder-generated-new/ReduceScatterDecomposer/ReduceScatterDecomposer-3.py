
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    return tf.xla.experimental.reduce_scatter(x, tf.constant(0), axis=0, use_global_device_ids=True, num_replicas=4, max_contraction=1)

# Initializing the model
m = Model()

# Inputs to the model
x = tf.constant([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0], [13.0, 14.0, 15.0, 16.0]])

# Call model
y = m(x)

print(y)  # Should print output, which is a distributed tensor across multiple devices