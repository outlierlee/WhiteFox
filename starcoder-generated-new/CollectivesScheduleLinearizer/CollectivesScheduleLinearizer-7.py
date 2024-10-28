
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.distribute.experimental.AllReduce(x1, colocate_across_devices=True, group=None)
    x3 = tf.distribute.experimental.AllGather(x2, axis=None, group=None)
    return x3

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
```
The above two models should ensure the optimization passes of ReshapeReshapeForwarding and CollectivesScheduleLinearizer in TensorFlow XLA can be triggered. Please make sure the `AllReduce` and `AllGather` operations in collective without explicitly specifying group or axis, instead relying on the semantics of the collective group.