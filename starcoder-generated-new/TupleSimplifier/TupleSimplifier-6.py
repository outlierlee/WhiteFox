
```python
class Model(tf.keras.Model):
    
    def __init__(self):
        super(Model, self).__init__()

    def call(self, x) -> tuple:
        t = tf.stack((x, x, x))
        a = tf.get_tuple_element(t, 0)
        return (a, a, a)
```

# Use
```python
m = Model()

# Input to the model
x = tf.constant([4.,5.,6.,7.], shape=[4])
result = m(x)
```