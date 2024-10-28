
class MyModel(tf.keras.Model):

  def __init__(self):
    super(MyModel, self).__init__()

  def call(self, x):
    sorted_tensor = tf.sort(x, axis=-1, direction='DESCENDING')
    result = tf.slice(sorted_tensor, [0, 0], [-1, 2])  
    return result

# Initializing the model
m = MyModel()

# Inputs to the model
input_shape = [2,3]
x = tf.constant([[1.0, 3.0, 2.0], [4.0, 6.0, 5.0]], shape=input_shape)

# Call model
y = m(x)
print(y.shape)