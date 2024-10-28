:
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.cast(x1, tf.float32)
    x3 = tf.cast(x2, tf.float64)
    return tf.cast(x3, tf.float64)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2]
x1 = tf.constant([1.2, 3.4], shape=input_shape)

# Call model
y = m(x1)  
This Python code defines a TensorFlow model with multiple consecutive cast operations. You can use the provided model and input to trigger the related optimization pass in TensorFlow XLA.