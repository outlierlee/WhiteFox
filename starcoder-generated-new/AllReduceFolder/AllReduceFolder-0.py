
class Model(tf.keras.Model):
    
  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.raw_ops.Reshape(tensor=x1, shape=[1, 4])
    return tf.raw_ops.Reshape(tensor=x2, shape=[4])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)

xla_model_string = tf.saved_model.save(m, './model')