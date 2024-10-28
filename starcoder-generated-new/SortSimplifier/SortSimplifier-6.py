

```python
class Model(tf.keras.Model):

    def __init__(self):
        super(Model, self).__init__()

    @tf.function
    def call(self, x):
        y = tf.sort((x[0], x[1], x[2]))
        return y[1] + y[2]

# Model Initialization
m = Model()

# Tuple Input to the model
x = ([5., 4., 3.], [7., 8., 9.], [1., 2., 3.])

# call model
y = m(x)
```

The model above will use `SortSimplifier` optimization pass if it is enabled in TensorFlow XLA.