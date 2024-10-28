
class Model(tf.keras.Model):

  def __init__(self, eliminate_type, replace_with_type):
    super(Model, self).__init__()
    self.eliminate_type = eliminate_type
    self.replace_with_type = replace_with_type
    moo_value = np.array([[1,2,3],[4,5,6]], dtype=self.eliminate_type)
    

  def call(self, x1):
    # Convert from eliminate_type to replace_with_type and back
    x2 = tf.math.add(x1, x1, name=None)
    x3 = tf.math.abs(x2, name=None)
    x4 = tf.cast(x3, self.eliminate_type, name=None)
    return x4


m = Model(tf.float32, tf.int32)

x1 = tf.constant([4.,5.,6.], shape=[3], dtype=m.eliminate_type)

y = m(x1)
```

Please generate a model that triggers the `HloElementTypeConverter` optimization pass while reusing public TensorFlow APIs. If you experiment with different data types, please also provide them to the `eliminate_type_` and `replace_with_type_` constructors.