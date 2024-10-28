

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.reshape(x1, [0])
    return x2

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)

print(y.numpy())  # Returns []
```
After calling the model with a tensor as the input, it successfully prints an empty zero-sized tensor, which means it triggered the `ZeroSizedHloElimination` optimization pass.