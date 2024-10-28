
```python
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    x1 = tf.transpose(x1, perm=[1, 0])
    x2 = tf.transpose(x2, perm=[1, 0])
    conv = tf.nn.conv1d(x1, x2, padding='SAME')
    return conv

# Initializing the model
m = Model()

# Input tensors to the model
input_shape = [4, 2]
x1 = tf.constant([[4.,5.], [6.,7.], [10.,11.], [12.,13.]], shape=input_shape)
x2 = tf.constant([[8.,9.], [14.,15.]], shape=[2, 1, 4])

# Call model
y = m(x1, x2)
```
It is important to note that the meaning of the model changes according to the transposes, and the actual computation performed by the model might be different from what is displayed in the code. As an example, before running the model, the TensorFlow XLA compiler optimizes to fold the transposes into the 1D convolution, if it is possible.