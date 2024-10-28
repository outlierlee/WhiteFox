
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

    self.var = tf.Variable(0.)

  def call(self, x):
    i = tf.constant(0)
    limit = tf.constant(10)

    def loop_body(i):
      # read operation (tf.identity is used to make sure there's no constant prop)
      read_val = tf.identity(self.var)
      # write operation (triggers control dependencies)
      new_val = tf.add(self.var, 1.)
      self.var.assign(new_val)
      return i + 1

    _, final_var = tf.while_loop(
        cond=lambda i: tf.less(i, limit), body=loop_body, loop_vars=[i, self.var])

    return final_var

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [1]
x = tf.ones(shape=input_shape, dtype=tf.int32)

# Call model
y = m(x)