:
class Model(tf.keras.Model):
  
  def __init__(self):
    super(Model, self).__init__()
    self.layernorm = tf.keras.layers.LayerNormalization(3.)
    self.add = tf.keras.layers.Add()

  def call(self, x1, x2):
    y1 = self.layernorm(x1)
    y2 = self.layernorm(x2)
    return self.add([y1, y2])

# Initializing the model
m = Model()

# Inputs to the model
input1_shape = [4]
input2_shape = [4]
x1 = tf.constant([0.9, 1.1, 3.3, 0], shape=input1_shape)
x2 = tf.constant([2.1, 2.3, 4.9, 0.5], shape=input2_shape)

# Call model
y = m(x1, x2)

# Run `HloConstantFolding` optimization pass
if tf.compat.v1.run_constant_folding().run(m):
  print("Changes have been made to model during constant folding optimization pass.")
else:
  print("No changes have been made to the model during constant folding optimization pass.")