
Class Model(tf.keras.Model):
  
  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    c1 = tf.constant([1, 2, 3, 4, 5])
    c2 = tf.constant([1, 2, 3, 4, 5])
    add_res1 = tf.add(c1, c2)
    add_res2 = tf.add(c1, c2)
    
    return add_res1, add_res2

# Initializing the model
m = Model()

# Inputs to the model
x = tf.constant([1, 2, 3, 4, 5])

# Call model
y1, y2 = m(x)

print("y1: ", y1)
print("y2: ", y2)