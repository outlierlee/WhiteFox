

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, a, b, c):
    t = tf.stack([a, b, c])
    a1 = tf.gather(t, [0])
    a2 = tf.gather(a1, [0])
    return tf.gather(a2, [0])

# Initializing the model
m = Model()

# Inputs to the model
a = tf.constant([1,2,3,4])
b = tf.constant([5,6,7,8])
c = tf.constant([9,10,11,12])

# Call model
y = m(a, b, c)

print(y)
```