

```python
class Model(tf.keras.Model):

    def __init__(self):
        super(Model, self).__init__()

    @tf.function(input_signature=[
        tf.TensorSpec(shape=[4], dtype=tf.float32),
        tf.TensorSpec(shape=[4], dtype=tf.float32),
    ])
    def call(self, x1, x2):
        return tf.raw_ops.StochasticConvert(x1, x2)

# Initializing model
m = Model()
```

