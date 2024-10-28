
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    self.slice = tf.slice
    self.add = tf.add
    self.shape1 = [6]
    self.indices1 = [1,0]
    self.shape2 = [4]
    self.indices2 = [2,0]

  def call(self, x1, x2):
    t1 = self.slice(x1, self.indices1, self.shape1)
    t2 = self.slice(x2, self.indices2, self.shape2)
    t3 = self.add(t1, t2)
    return t3

# Initializing the model
m = Model()

# Inputs to the model
input_shape1 = [6]
x1 = tf.constant([1.,2.,3.,4.,5.,6.], shape=input_shape1)
input_shape2 = [4]
x2 = tf.constant([7.,8.,9.,10.], shape=input_shape2)

# Call model
y = m(x1, x2)

# Print model architecture
print(m.summary())