
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.broadcast_to(x1, [4,4])
    return tf.all_gather(x2, [0, 1])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
```

# Final Output
The final output of these models will be:

```
Tensor('add:0', shape=(4,), dtype=float32)
```