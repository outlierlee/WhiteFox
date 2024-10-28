
```
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self):
    def condition(x, const_value):
      return x[0] < 10

    def body(x):
      return (x[0] + 1, x[1])

    tf.while_loop(condition, body, (tf.constant(0), tf.constant(10)))
```
Running the above model:
```python
model = Model()
model.call()
```
Here, `tf.constant(10)` won't change across the loop iterations and it is allowed to sink it into the loop's condition and body.