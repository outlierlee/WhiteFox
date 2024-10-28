
```python
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    x3 = tf.add(x1, x2)
    x4 = tf.cast(x3, tf.int32)
    return tf.cast(x4, x1.dtype)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [3]
x1 = tf.constant([1,2,3], shape=input_shape)
x2 = tf.constant([4,5,6], shape=input_shape)

# Call model
y = m(x1, x2)
```

IMPORTANT: Please make sure the produced model performs the operations defined in the description above since converting a model to TensorFlow XLA compilation might not produce the expected results otherwise.