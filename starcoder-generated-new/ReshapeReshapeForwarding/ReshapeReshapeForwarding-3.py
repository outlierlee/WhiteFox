
You can use a simple custom model for this, although simple models aren't very useful in practical machine learning scenarios, as they often rely on layers that are not supported by XLA optimization.

Here is an example of a model that performs the mentioned operations:

```python
class CustomModel(tf.keras.Model):

  def __init__(self):
    super(CustomModel, self).__init__()

  def call(self, x1):
    x2 = tf.reshape(x1, [2, 2])
    return tf.reshape(x2, [4])

# Initializing the model
m = CustomModel()
# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
# Call model
y = m(x1)
```

In this model, we used TensorFlow's reshaping functionality to create this specific pattern. The call method in this model, when called with some input(x1), will return the output of the second reshaping operation. The meaning of each tensor depends on the source tensor, in this case, it is the input tensor itself. When the pair of the first and second reshaping operation pattern appears in a model, the TensorFlow XLA compiler will trigger to transform this pattern into optimization that may improve the performance.