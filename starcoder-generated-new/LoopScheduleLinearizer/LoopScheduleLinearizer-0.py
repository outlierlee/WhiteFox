
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    def body(x, condition):
      # read operation
      def read(x):
        x = tf.random.uniform([1])
        return x, condition -1

      # write operation
      def write(x, condition):
        x = tf.add(x, tf.random.uniform([1]))
        return x, condition -1

      tf.cond(tf.greater(condition, 0), lambda: read(x), lambda: write(x, condition))

    _, _ = tf.while_loop(lambda condition: tf.greater(condition, 0), body, (x, 500))
    return x

# Initializing the model
m = Model()

# Inputs to the model
initial_value = tf.constant([1.0])

# Call model
y = m(initial_value)