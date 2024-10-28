

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    t = (x[0]+1, x[1]+2) # Shapes: ((4,4), (5,5))
    a1 = tf.get_tuple_element(t, 0) # Shapes: (4,4)
    a2 = tf.get_tuple_element(a1, 0) # Shapes: 4
    t1 = (a2 + 3,) # Shapes: (4,)
    return t1[0] # Shapes: ()

# Creating the model
m = Model()

# Creating input to the model
x = [tf.constant([[1, 2], [3, 4]], shape=(2, 2)), tf.constant([1, 2, 3, 4, 5], shape=(5,))]

# Call the Model
y = m(x)
```