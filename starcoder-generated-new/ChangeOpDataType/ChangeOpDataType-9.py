
```python
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    
  def call(self, x1, x2, x3):
    o1 = tf.math.add(x1, x2)
    o2 = tf.math.add(o1, x3)
    
    r1 = tf.reshape(o2, [4])
    
    return tf.cast(r1, tf.float32),

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([1.,2.,3.,4.], shape=input_shape, dtype=tf.int32)
x2 = tf.constant([4.,5.,6.,7.], shape=input_shape, dtype=tf.float32)
x3 = tf.constant([1.,2.,3.,4.], shape=input_shape, dtype=tf.float32)

# Call model
y = m(x1, x2, x3)
```

