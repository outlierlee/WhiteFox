
class Model(tf.keras.Model):

  loop_counter = tf.constant(0)

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    while_counter = 0

    @tf.function
    def condition(i, x1):
      return i < 10

    @tf.function
    def body(i, x1):
      nonlocal while_counter
      while_counter += 1
      return i+1, x1, while_counter

    while_counter = tf.constant(0)
    _, _, while_counter = tf.while_loop(condition, body, [while_counter, x1, tf.constant(3)])
    
    return while_counter

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
print(y)