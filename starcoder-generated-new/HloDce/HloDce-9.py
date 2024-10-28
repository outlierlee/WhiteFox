

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    t1 = tf.multiply(x, x)  # This computation is not used
    t2 = tf.add(x, x)  # This computation will be removed if remove_cross_partition_collective_ops is True
    scream = self.scream()
    return tf.multiply(x, x)  # This computation is useful

  @tf.function
  def scream(self):
    print()  # This computation will be made non-recursive


# Initializing the model
m = Model()

# Call model
x = tf.constant([1.,2.,3.,4.], shape=[4])

m(x)