

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x1 = tf.assign(x1, tf.some_operation(x1))
    return tf.while_loop(lambda xx: xx < 10, (lambda xx: tf.assign(xx, xx + 1)), [x1])[0]

# Initializing the model
m = Model()

# Inputs to the model
initial_value = tf.constant(0.)

# Call model
y = m(initial_value)
```
This is a very basic version and we can bring it more complicated if necessary. TensorFlow XLA uses the Zeta abstraction, basically it does not have a tf.Variable unlike in eager mode. So to make a simple tensor to behave like a tf.Variable you assign the operation in the loop body to the tensor.

Note: In this example, we use level 1 and level 2 controls but we could go deeper and need more type of control dependencies. Please remember this, the point is to use them correctly to prevent potential data races within a loop.