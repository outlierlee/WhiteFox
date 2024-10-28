

Create a class Model defines two operations associating on TensorFlow model.

```python
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    t1 = tf.reduce_sum(x1, axis=[1,2])
    t2 = tf.reduce_sum(x2, axis=[1,2])
    t3 = tf.add(t1, t2)
    return t3

# Initializing the model
m = Model()

# Inputs to the model
input1_shape = [4, 4, 4]
input2_shape = [4, 4, 4]
x1 = tf.random.normal(input1_shape)
x2 = tf.random.normal(input2_shape)

# Call model
y = m(x1, x2)
```
The above model is a simple example which meets all given requirements. The essence is creating two TensorFlow reduce functions (`reduce_sum` and `add` here) applied to the input tensors `x1` and `x2`, respectively.