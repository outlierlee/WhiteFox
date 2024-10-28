:
class Model(tf.keras.Model):
  
  def __init__(self):
    super(Model, self).__init__()

  def true_fn(self):
    return tf.constant(1, dtype=tf.int32)
    
  def false_fn(self):
    return tf.constant(0, dtype=tf.int32)

  def call(self, x):
    return tf.cond(tf.reduce_sum(x) > 10, self.true_fn, self.false_fn)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [10]
x = tf.constant([10.,]*10, shape=input_shape)

# Call the model
y = m(x)

# Printing the output
print(y)