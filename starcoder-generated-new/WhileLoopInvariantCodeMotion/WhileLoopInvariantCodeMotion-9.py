
Here is one such model:

```python
class MyModel(tf.keras.Model):
    def __init__(self):
        super(MyModel, self).__init__()

    def call(self, x):
        # invariant instruction Inside the loop
        def loop_body(x):
            # Note the invariant instruction
            y = tf.constant(5)
            z = tf.add(x, y)
            return z

        z = tf.constant(0)
        result = tf.while_loop(lambda x: tf.less(x, 10), loop_body, [z])
        return result

model = MyModel()
model(tf.constant(100))
```

This model contains while_loop with invariant computation and will be triggering the optimization pass.