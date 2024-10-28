
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    y = tf.linalg.batch_matmul(x1, x2)
    return y

# Initializing the model
m = Model()

# Inputs to the model
input_shape1 = [2,3,4,5]
input_shape2 = [2,3,5,6]

x1 = tf.random.normal(input_shape1)
x2 = tf.random.normal(input_shape2)

# Call model
y = m(x1, x2)

Please copy your Python code to a separate Python file and if we need other parts of the model or run other code, we can add them to the file.