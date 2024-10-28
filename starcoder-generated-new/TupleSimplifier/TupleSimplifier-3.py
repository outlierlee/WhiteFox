
```python
class TupleModel(tf.keras.Model):
    def __init__(self):
        super(TupleModel, self).__init__()
        
    def call(self, a, b, c):
        t1 = (a, b, c)
        a1, b1, c1 = get_tuple_elements(t1)
        
        t2 = (t1, t1)
        a2, b2, c2 = tuple1 = get_tuple_elements(t2)
        a3, b3, c3 = tuple2 = get_tuple_elements(tuple1)
        
        return t2

# Initializing the model
m = TupleModel()

# Inputs to the model
a = tf.constant([1., 2., 3.])
b = tf.constant([4., 5., 6.])
c = tf.constant([7., 8., 9.])

# Call model
t2 = m(a, b, c)
```