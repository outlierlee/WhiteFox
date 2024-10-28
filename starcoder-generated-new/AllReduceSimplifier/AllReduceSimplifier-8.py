

class CustomModel(tf.keras.Model):
  def __init__(self):
    super(CustomModel, self).__init__()
	  # Model layers defined here....

  def call(self, x):
    # Model computation defined here....
    r = tf.distribute.experimental.Reduce(reduction="add", num_partitions=2)
    x = tf.distribute.all_gather(x)
    x = r(x)
    x = tf.distribute.all_reduce(x, "add", group="group1")
    x = tf.distribute.reduce_scatter(x, "minimum", group="group2")
    return x

m = CustomModel()
input_shape = [4]
x = tf.constant([4.,5.,6.,7.], shape=input_shape)

y = m(x)

