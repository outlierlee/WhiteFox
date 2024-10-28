

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    i, c = tf.constant(0), tf.constant(2)
    def condition(i, c): return i < 10
    def body(i, c): return i+1, c
    return tf.while_loop(condition, body, [x1, c])

m = Model()
x1 = tf.constant([4])
y = m(x1)
print(y)


