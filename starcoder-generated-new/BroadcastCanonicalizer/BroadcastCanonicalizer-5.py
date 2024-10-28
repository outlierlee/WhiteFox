:
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    return tf.broadcast_to(x1, [4,4,5])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4,4,1]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)


Here, our generated model `Model` is a subclass of `tf.keras.Model`, and it overrides the `call` method. The `call` method contains the `tf.broadcast_to` operator, which broadcasts the tensor `x1` to a new shape of `[4,4,5]`.

This is the minimum requirement to trigger the `BroadcastCanonicalizer` optimization pass in TensorFlow XLA. If the user does not sort the dimensions of broadcast fully and has some unrelated operation/reshape operation between them then the optimization can fail.