
class MyModel(tf.keras.Model):

  def __init__(self):
    super(MyModel, self).__init__()

  def call(self, x):
    def true_fn():
      return tf.constant(1, shape=x.shape)

    def false_fn():
      return tf.constant(0, shape=x.shape)

    return tf.cond(tf.constant(True), lambda: true_fn(), lambda: false_fn())

# Initializing the model
m = MyModel()

# Inputs to the model
x = tf.constant([1,1,1,1])

# Call model
y = m(x)
print(y)