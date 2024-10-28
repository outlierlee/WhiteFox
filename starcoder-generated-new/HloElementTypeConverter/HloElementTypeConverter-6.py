

```python
class EntryPointModel(tf.keras.Model):
  def __init__(self):
    super(EntryPointModel, self).__init__()
    
  def call(self, inputs):
    x = inputs['x']
    y = inputs['y']
    z = tf.function(lambda x, y: x + y)(x.cast(tf.dtypes.int32), y.cast(tf.dtypes.int32))
    return z
```

# Inputs
```python
inputs = {
    'x': tf.constant([1, 2, 3], dtype=tf.float32),
    'y': tf.constant([4, 5, 6], dtype=tf.float32),
}
```

# Output
The expected output of the model is `15`, but it should be `[2, 4, 6]` due to `tf.int32` instead of `tf.float32` datatype.