

```python
import tensorflow as tf

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    x_sorted = tf.sort(x)
    return x_sorted[0] + x_sorted[1] # Here we only use the first two elements of the sorted list

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x = tf.constant([4.,5.,6.,7.], shape=[4])

# Call model
y = m(x)
```