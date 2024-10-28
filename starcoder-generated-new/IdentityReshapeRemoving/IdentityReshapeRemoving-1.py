
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    return tf.reshape(x1, x1.shape)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)

The model is just a simple linear model with a reshape added in the middle for the test.

```python
#Model :
class Model(tf.keras.Model):
    
  def __init__(self):
    super(Model, self).__init__()
    self.linear_layer = tf.keras.layers.Dense(4)
    
  def call(self, x1):
    x = tf.reshape(x1, [2,2])
    return self.linear_layer(x)

m = Model()
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
y = m(x1)
```

That's it.