
```python
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2, x3):
    sorted_tuple = tf.sort((x1, x2, x3))
    return some_function(sorted_tuple[0], sorted_tuple[1])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x2 = tf.constant([1.,2.,3.,4.], shape=input_shape)
x3 = tf.constant([0.,7.,8.,10.], shape=input_shape)

# Call model
y = m(x1, x2, x3)
```
In the above model, `x3`, even though it's sorted (as long as `x1` and `x2` have the same values), is not used directly in the computation, so `SortSimplifier` should be able to remove that operation.