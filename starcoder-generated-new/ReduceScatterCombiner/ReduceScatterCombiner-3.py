
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

    self.r1 = tf.raw_ops.ReduceScatter(name="reduce_scatter1")
    self.r2 = tf.raw_ops.ReduceScatter(name="reduce_scatter2")
  
  def call(self, x1, x2):
    y1 = self.r1(x1, "add",axis=[1])
    y2 = self.r2(x2, "add",axis=[1])
    
    return y1+y2

# Initializing the model
m = Model()

# Inputs to the model
input_shape1 = [2,2]
input_shape2 = [2,2]
x1 = tf.ones(input_shape1)
x2 = tf.ones(input_shape2)

# Call model
y = m(x1,x2)

print(y)
```
Please note that the parameters need to be changed according to the needs of each model and environment. Replace `'add'` and `axis=[1]` with actual parameters for your specific use-case scenario.