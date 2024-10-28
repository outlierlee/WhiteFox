
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, a, b, c):
    t = tf.tuple([a, b, c])
    a1 = tf.get_tuple_element(t, 0)
    a2 = tf.get_tuple_element(t, 0)
    a3 = tf.get_tuple_element(t, 0)
    return a1, a2, a3

# Creating and running the model
model = Model()
outputs = model(tf.constant([1.,2.,3.]), tf.constant([4.,5.,6.]), tf.constant([7.,8.,9.]))