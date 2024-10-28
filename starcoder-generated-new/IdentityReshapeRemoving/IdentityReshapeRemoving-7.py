
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    return tf.reshape(x1, x1.shape)

# Initialize the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([1.,2.,3.,4.], shape=input_shape)

# Call model
y = m(x1)

# Print the output
print(y.numpy())