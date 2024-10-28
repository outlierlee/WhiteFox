

```python
import tensorflow as tf

class Model(tf.keras.Model):

    def __init__(self):
        super(Model, self).__init__()
        self.n = tf.Variable(0.)

    def call(self, x):
        if self.n % 2 == 0:
            x = self.dead_computation(x)
            self.n.assign(self.n + 1.)
            x = tf.reduce_sum(x)
        else:
            self.n.assign(self.n + 1.)
            x = self.dead_computation(x)
            x = tf.reduce_sum(x)
        return x

    @tf.function
    def dead_computation(self, x):
        y = tf.add(x, x)  # This computation is not used anywhere
        return tf.multiply(x, x) - y
```
Here the dead computation `dead_computation(x)` is being used nowhere in the model and raises a computation error during optimization when the scope of `dead_computation(x)` is ???(addtion of dead computation here).