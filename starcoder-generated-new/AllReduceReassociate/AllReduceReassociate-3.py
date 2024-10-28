
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

    self.axis = 0
    self.operation = 'add'

  def call(self, x1, x2):
    t1 = tf.raw_ops.AllReduce(x1, self.operation, indices='', group_assignment='', axis=self.axis)
    t2 = tf.raw_ops.AllReduce(x2, self.operation, indices='', group_assignment='', axis=self.axis)
    t3 = tf.raw_ops.AddN([t1, t2])
    return t3

# Initializing the model
m = Model()

# Creating inputs
input_shape = [4]
x1 = tf.constant([4., 5., 6., 7.], shape=input_shape)
x2 = tf.constant([7., 8., 9., 10.], shape=input_shape)

# Call model
y = m(x1, x2)
