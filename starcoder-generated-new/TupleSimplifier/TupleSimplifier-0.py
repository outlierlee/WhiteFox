
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    t = tf.tuple([x1, x1, x1])  # First pattern
    a1 = tf.get_tuple_element(t, 0)
    b1 = tf.get_tuple_element(t, 1)
    c1 = tf.get_tuple_element(t, 2)
    t1 = tf.tuple([a1, b1, c1])  # Pair of GetTupleElement followed by Tuple

    x2 = tf.get_tuple_element(a1, 0) # First GetTupleElement followed by GetTupleElement
    x3 = tf.get_tuple_element(x2, 0) # Second GetTupleElement
    return x3

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [1]
x1 = tf.constant([4.], shape=input_shape)

# Call model
y = m(x1)
print(y)