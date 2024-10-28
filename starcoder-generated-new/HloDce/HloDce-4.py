
```python
class Model(tf.keras.Model):

    def __init__(self):
        super(Model, self).__init__()

    def call(self, x1):
        x2 = tf.subtract(x1, x1)  # Dead computation
        return x2
```

