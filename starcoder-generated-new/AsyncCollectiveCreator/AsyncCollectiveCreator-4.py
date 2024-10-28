
class AsyncModel(tf.keras.Model):

  def __init__(self):
    super(AsyncModel, self).__init__()
    
  def call(self, x):
    reduce_endpoints = x.shape[-1]
    reduce_function = x[0]
    reduce_groups = x[1]
    out = tf.raw_ops.CollectiveCommunications(group_key=reduce_groups, function=reduce_function, devices=reduce_endpoints, name=None)
    return out

# Initializing the model
async_model = AsyncModel()

# Inputs to the model
input_shape = [2,4]
x = tf.constant([[4.,5.,6.,7.],[8.,9.,10.,11.]], shape=input_shape)
    
# Call model
y = async_model(x)
```