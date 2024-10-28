
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    return tf.zeros([0])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)

print(y)

The above model would effectively do nothing and return an empty Tensor of shape `[0]`. Any model (such as one that uses the `tf.zeros` operation) that matches the example description should trigger the `ZeroSizedHloElimination` optimization pass if we prevent the division by zero then zero during the tensor reshaping operations and replace the operations with constants at compile time.