
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    counter = tf.constant(0, dtype=tf.int32)
    result = tf.constant(0, shape=x.shape, dtype=x.dtype)
    cond = lambda counter, result: tf.less(counter, tf.constant(10))

    def body(counter, result):
      read = tf.cond(tf.less(counter, tf.constant(5)), lambda: tf.identity(x), lambda: tf.zeros_like(x))      
      write = tf.assign(result, read)
      update_counter = tf.add(counter, 1)
      return update_counter, write

    with tf.control_dependencies([body(counter, result)[1]]):
      counter, result = tf.while_loop(cond, body, [counter, result])

    return result

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x)
```
Please note that TensorFlow XLA can potentially optimize the model to access the same memory location only once, instead of ten times. If the problem to be solved is computational intense enough, we can always wait for TensorFlow to optimize these types of operations even further.