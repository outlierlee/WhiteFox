
class Model(tf.keras.Model):

  def __init__(self, device_mesh):
    super(Model, self).__init__()
    self.device_mesh = device_mesh
  
  def call(self, x1):
    y1 = tf.raw_ops.AllToAll(x1, shape=x1.shape, device_mesh=self.device_mesh)
    y2 = tf.raw_ops.CollectivePermute(y1, device_mesh=self.device_mesh)
    return y2

# Generate device mesh
device_mesh = DeviceMesh(device_mesh="", mesh_shape="") 

# Initializing the model
m = Model(device_mesh)

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)

# Expected output
# y == the output tensor from the operation

