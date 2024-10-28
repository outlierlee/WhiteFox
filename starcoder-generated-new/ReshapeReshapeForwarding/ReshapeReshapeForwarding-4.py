
```python
class Model(tf.keras.Model):
  def __init__(self, input_shape=[8]):
    super().__init__()
    self.layer1 = tf.keras.layers.Reshape((2,2), input_shape=input_shape)
    self.layer2 = tf.keras.layers.Reshape(input_shape)

  def call(self, x):
    x = self.layer1(x)
    x = self.layer2(x)
    return x

x = tf.constant([i for i in range(8)], shape=[2, 2, 2])  # Create a rank 3 Constant tensor

m = Model()
y = m(x)
```

# Expected output
You will see `ReshapeReshapeForwarding` happening at the time of execution of the model and any optimization passes. Please note that this may depend on the specific TensorFlow version being used, the TensorFlow process environment, and other factors.