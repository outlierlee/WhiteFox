
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    self.iota = tf.Variable(tf.range(100))

  def call(self, x):
    sorted_tensor = tf.sort(x, direction='DESCENDING')
    top_k_tensor = tf.slice(sorted_tensor, [0, 0], [-1, -1])
    return top_k_tensor

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [8,4]
x1 = tf.constant([103., 99., 95., 91., 87., 83., 79., 75.,        
                  71., 67., 63., 59., 55., 51., 47., 43.,
                  39., 35., 31., 27., 23., 19., 15., 11.,
                  7.,  3.,  1.], shape=input_shape)

# Call model
y = m(x1)