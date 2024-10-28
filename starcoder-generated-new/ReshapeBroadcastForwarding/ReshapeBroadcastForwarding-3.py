
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    x1 = tf.broadcast_to(x, [1])
    return tf.reshape(x1, [])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = []
x = tf.constant([3.5], shape=input_shape)

# Call model
y = m(x)
``` 

Note:
1. We shoud use `tf.broadcast_to` to transform `input_tensor` to a one-dimensional tensor, then use `tf.reshape` to transform this one-dimensional tensor back to a scalar.
2. We should use only public TensorFlow APIs (no keras, eager execution) because this script needs to be cross-compatible with TensorFlow versions up to 1.15.
3. Each model should accept the same input (a scalar Tensor) and produce the same output (a scalar Tensor).