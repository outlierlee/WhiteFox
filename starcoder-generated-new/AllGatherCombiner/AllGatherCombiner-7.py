
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2, x3):
    x1_gather = tf.distribute.AllGather(x1, axis=0)
    x2_gather = tf.distribute.AllGather(x2, axis=1)
    x3_gather = tf.distribute.AllGather(x3, axis=2)
    return (x1_gather, x2_gather, x3_gather)

# Initializing the model
m = Model()

# Inputs to the model
input_shape1 = [2,2]
input_shape2 = [2,2]
input_shape3 = [2,2]

x1 = tf.constant([[4.,5.],[6.,7.]], shape=input_shape1)
x2 = tf.constant([[4.,5.],[6.,7.]], shape=input_shape2)
x3 = tf.constant([[4.,5.],[6.,7.]], shape=input_shape3)

# Call model
y = m(x1, x2, x3)

print(y[0])
print(y[1])
print(y[2])