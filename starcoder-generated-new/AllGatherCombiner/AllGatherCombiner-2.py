

Assuming we have n total AllGather operations and the operations are disjointed among different tensors.
```
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    self.all_gather_dimension = [0]

  def call(self, x_list):
    all_gather_ops = []
    for x in x_list:
      all_gather_op = tf.distribute.AllGather(x, self.all_gather_dimension)
      all_gather_ops.append(all_gather_op)
    return all_gather_ops

# Initializing the model
m = Model()

# Inputs to the model
x1 = tf.constant([1])
x2 = tf.constant([2])
x_list = [x1, x2]

# Call model
y_list = m(x_list)
```
Here, the model consists of two AllGather operations. For each input tensor, the model calls AllGather to gather all tensors that come in the input and outputs each single gather tensor as a separate element of the output list.