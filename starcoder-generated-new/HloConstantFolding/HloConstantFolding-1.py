
class MyModel(tf.keras.Model):

  def __init__(self):
    super(MyModel, self).__init__()

  def call(self, x):
    # Constant size multiple of the input tensor which would not cause a large constant size and make constant folding easier
    tensor_size = [2, 2, 2, 2]
    const_tensor = tf.constant([1., 2., 3., 4.], shape=tensor_size)

    x = tf.broadcast_to(x, tensor_size)
    x = tf.abs(x - const_tensor)

    return x

# Get your model and input
model = MyModel()
input_tensor = tf.constant([1,2,3], shape=[3])

# Call and check if constant folding changes the computation graph
before = model(input_tensor)
constant_folding_runs = model.optimize(constant_folding=True)
after = model(input_tensor)

print("Constant Folding Runs: ", constant_folding_runs)
print("Input: ", input_tensor)
print("Before: ", before)
print("After: ", after)