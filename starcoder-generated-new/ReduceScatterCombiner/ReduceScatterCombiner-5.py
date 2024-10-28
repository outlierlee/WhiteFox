
# Define a model with multiple tf.raw_ops.ReduceScatter operations

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2, x3):
    y1 = tf.raw_ops.ReduceScatter(input=x1, reduction_op='add', ...)
    y2 = tf.raw_ops.ReduceScatter(input=x2, reduction_op='add', ...)
    y3 = tf.raw_ops.ReduceScatter(input=x3, reduction_op='add', ...)

    return y1, y2, y3
  
# initialize the model 
m = Model()

# define inputs 
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x2 = tf.constant([10., 20., 30., 40.], shape=input_shape)
x3 = tf.constant([-1.,-2.,-3.,-4.], shape=input_shape)

# Call model
y1, y2, y3 = m(x1, x2, x3)