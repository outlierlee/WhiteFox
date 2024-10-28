
```python
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    
  def call(self, x1):
    # Creates a tuple [x1, x1, x1]
    t1 = tf.tuple([x1, x1, x1])
    
    # Extracts the element at index 0
    a1 = tf.get_tuple_element(t1, 0)

    # Creates a tuple [a1, a1, a1]
    t2 = tf.tuple([a1, a1, a1])
    
    return t2
```

# Usage
m = Model()
input_shape = [2]
x1 = tf.constant([2.,3.], shape=input_shape)
y = m(x1)

**The above model should pass `TupleSimplifier` in TensorFlow XLA.**