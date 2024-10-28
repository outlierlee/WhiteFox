

```python
class Model(tf.keras.Model):

    def __init__(self):
      super(Model, self).__init__()

    @staticmethod
    def get_true_fn():
        return tf.constant(1)

    @staticmethod
    def get_false_fn():
        return tf.constant(0)

    def call(self, x1):
        return tf.cond(tf.constant(True), self.get_true_fn, self.get_false_fn)

m = Model()
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
y = m(x1)
```
Please export this model to TensorFlow Lite format and confirm whether it triggers the `ConditionalCanonicalizer` optimization pass when being passed through TensorFlow XLA compiler.