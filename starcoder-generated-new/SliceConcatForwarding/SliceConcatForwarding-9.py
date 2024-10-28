
```python
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    
  def call(self, x1, x2, start_index):
    x3 = tf.concat([x1, x2], 0)
    return tf.slice(x3, [start_index], [tf.size(x3)-start_index])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2, 2]
x1 = tf.constant([2.,3.,4.,5.], shape=input_shape)
x2 = tf.constant([6.,7.,8.,9.], shape=input_shape)
start_index = 4

# Call model
y = m(x1, x2, start_index)
```


