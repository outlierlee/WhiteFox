
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2, x3, x4):
    x1_agg = self.aggregator([x1])
    x2_agg = self.aggregator([x2])
    x3_agg = self.aggregator([x3])
    x4_agg = self.aggregator([x4])
    
    all_agg_combined = self.aggregator([x1_agg, x2_agg, x3_agg, x4_agg])

    return all_agg_combined

  def aggregator(self, tensors):
    combined_tensors = tf.concat(tensors, axis=0)
    all_gather_op = tf.distribute.AllGather(combined_tensors)
    return all_gather_op

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x2 = tf.constant([8.,9.,10.,11.], shape=input_shape)
x3 = tf.constant([12.,13.,14.,15.], shape=input_shape)
x4 = tf.constant([16.,17.,18.,19.], shape=input_shape)

# Call model
y = m(x1, x2, x3, x4)

print(y)