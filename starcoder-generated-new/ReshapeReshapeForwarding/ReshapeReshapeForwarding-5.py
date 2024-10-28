
Class Model(tf.keras.Model):
  
  def __init__(self):
    super(Model, self).__init__()
  
  def call(self, x):
    t1 = tf.reshape(x, [4,1])
    return tf.reshape(t1, [4])
    
# Initializing the model 
m = Model()

# Testing inputs
x = tf.constant([1.0,2.0,3.0,4.0])

y = m(x)

