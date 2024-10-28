
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.broadcast_to(x1, [1])
    return tf.reshape(x2, [])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = []
x1 = tf.constant([4], shape=input_shape)

# Call model
y = m(x1)
```

Note: The generated models need to be runnable and does not require to any other additional library or package. Only TensorFlow and no other tool/package is used other than TensorFlow, to keep the models as constrained as possible. The model configurations can be changed according to that particular optimization pass requirement.