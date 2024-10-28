
```python
class Model(tf.keras.Model):
  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    i = tf.constant(0)
    c = lambda i: tf.less(i, 10)
    b = lambda i: tf.add(i, 1)
    r = tf.while_loop(c, b, [i])
    print("Loop executed", r)
```
# Initializing the model
```python
m = Model()

# Call model
m(tf.constant(0))
```
In this model we create a `while` loop where we increment `i` by 1 until it reaches 10. After running the model (by calling it with an initial `i` of 0) the print statement will print out that the `while` loop executed 10 times. This will trigger the `WhileLoopTripCountAnnotator` optimization pass in TensorFlow XLA.