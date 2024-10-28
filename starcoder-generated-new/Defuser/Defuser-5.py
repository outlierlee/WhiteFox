:
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  @tf.function(experimental_compile=True)
  def call(self, x):
    x = x * tf.math.sin(x)
    return x
```
