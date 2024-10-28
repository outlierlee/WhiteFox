
class MyModel(tf.keras.Model):

  def __init__(self):
    super(MyModel, self).__init__()

  def call(self, x):
    h = tf.constant([[1,2,3],[4,5,6],[7,8,9]], dtype=tf.float32)
    rhs0 = tf.Variable([1,2,3], dtype=tf.float32)
    rhs1 = tf.Variable([1,2,3], dtype=tf.float32)

    return tf.linalg.matmul(h, rhs0), tf.linalg.matmul(h, rhs1)

# Initializing the model
m = MyModel()

# Inputs to the model
x = [1,2,3]

# Call model
y = m(x)

Please generate one valid TensorFlow model that satisfies requirements below. The model can be used as the input to trigger the optimization pass `RightHandSideInliner` in TensorFlow XLA.

# Description
The model should contain a right-hand-side operand (rhs) in `matmul` operation that is not a Variable or Constant but an arbitrary operation with side-effects (e.g., a function call). 

This pattern is used to test the `RightHandSideInliner` optimization pass. In this case, it doesn't reduce the computational complexity or memory usage compared to a lambda or tf.function, but it does to annotate the rhs when we attempt to optimize away the rhs operation.

# Model
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    h = tf.constant([[1,2,3],[4,5,6],[7,8,9]], dtype=tf.float32)
    rhs = lambda: tf.Variable([1,2,3], dtype=tf.float32)

    return tf.linalg.matmul(h, rhs())

# Initializing the model
m = Model()

# Inputs to the model
x = [1,2,3]

# Call model
y = m(x)
y