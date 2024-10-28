
```python
class Model(tf.keras.Model):
    
    def __init__(self):
        super(Model, self).__init__()

    def call(self, x1):
        def condition(iter, x):
            return tf.less(x, 10)

        def body(iter, x):
            return tf.add(iter, 1), tf.add(x, 1)

        result = tf.while_loop(condition, body, [tf.constant(0), x1])

        return result[0]

m = Model()

input_shape = [4]
x1 = tf.constant([1,2,3,4], shape=input_shape)

# Call model
y = m(x1)
```