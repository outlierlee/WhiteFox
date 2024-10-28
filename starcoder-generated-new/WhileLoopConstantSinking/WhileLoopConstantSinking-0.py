
class Model(tf.keras.Model):

  def __init__(self, iterations):
    super(Model, self).__init__()
    self.iterations = iterations

  def call(self, x1):

    def condition(i, x, y):
      return i < self.iterations

    def body(i, x, y):
      return i + 1, x + 1, y

    _, _, result = tf.while_loop(condition, body, (0, x1, 2)) 

    return result
    
# Initializing the model
m = Model(iterations=6)

# Inputs to the model
x1 = tf.constant([0.,1.,2.,3.,4.,5.], shape=[6])

# Call model
y = m(x1)
```
Shortly, Tensorflow XLA is an automatic differentiation (auto-diff) and optimization system for TensorFlow. XLA has optimizations targeted towards improving performance including unrolling loops, vectorizing, tiling code, more intelligent scheduling of computations and sinking of constants into loop, kernel operation and loop boundaries.