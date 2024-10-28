
class Model(tf.keras.Model):

  def __init__(self, N):
    super(Model, self).__init__()
    # Get a random input shape
    input_shape = np.random.randint(low=1, high=10, size=N)
    # Random input tensors
    self.inputs = [tf.Variable(np.random.randint(low=1, high=10, size=input_shape))]

  def call(self):
    # Collect the tensors
    tensors = [tf.reduce_sum(input_tensor) for input_tensor in self.inputs]
    # Combine the tensors
    combined = tf.add_n(tensors)
    return combined

# Initializing the model
m = Model(N=10)

# Call model
y = m()

# Checking the size of the operands
print("Operand size: ", tf.size(m.inputs[0]).numpy()*4)  # 4 is for 32-bit data type.