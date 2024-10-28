
# Define a model with multiple tf.distribute.AllGather operations. The model
# doesn't contain operations with all_gather_dimension=0 because it doesn't belong to the required model pattern.
 
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    self.layer1 = tf.distribute.MirroredStrategy().extended.all_gather([1,2,3])
    self.layer2 = tf.distribute.MirroredStrategy().extended.all_gather([4,5,6])
    self.layer3 = tf.distribute.MirroredStrategy().extended.all_gather([7,8,9])

  def call(self, x):
    return self.layer1(x), self.layer2(x), self.layer3(x)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x = tf.constant([4.,5.,6.,7.], shape=input_shape)
  
# Call model
y = m(x)