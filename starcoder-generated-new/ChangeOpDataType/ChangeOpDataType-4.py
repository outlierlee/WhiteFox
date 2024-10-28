
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    
  def call(self, x1):
    return tf.cast(tf.reduce_sum(x1), dtype=tf.int32)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4,4]
x1 = tf.constant([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], shape=input_shape)

# Call model
y = m(x1)
print(y)