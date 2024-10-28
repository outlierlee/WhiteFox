

# Following pattern along: Take a 2-D Tensor input, insert into the looping function body via a `while_loop`, and return the accumulated result.

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def condition(self, vars):
    # condition code
    return tf.reduce_any(tf.add(vars[0], 1) < 10)

  def body(self, vars):
    # body code
    # appending 1 to vars[0] for iterative computations
    new_var = tf.add(vars[0], 1)
    # This will be kept as a nested tuple, ensuring that all operations will remain within the while_loop
    return (new_var, vars[1])

  def call(self, input_tensor):
    x1, x2 = tf.split(input_tensor, 2, axis=1)
    x1 = tf.cast(x1, dtype=tf.int32)
    result = tf.while_loop(self.condition, self.body, [x1, x2])
    # result[1] is a constant or a broadcast of a constant
    return result[1]

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2, 2, 4]
x1 = tf.constant([[4.,5.],[6.,7.]], shape=input_shape)

# Call model
y = m(x1)