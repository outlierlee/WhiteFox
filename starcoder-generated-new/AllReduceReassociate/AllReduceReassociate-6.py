
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    x1_reduced = tf.reduce_sum(x1, axis=0)
    x2_reduced = tf.reduce_sum(x2, axis=0)
    return x1_reduced + x2_reduced

# Initializing the models
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x2 = tf.constant([1.,2.,3.,4.], shape=input_shape)

# Call model
y = m(x1, x2)
```
Please generate a single valid TensorFlow model that satisfies the requirements in the problem description. The model should only use public TensorFlow APIs.