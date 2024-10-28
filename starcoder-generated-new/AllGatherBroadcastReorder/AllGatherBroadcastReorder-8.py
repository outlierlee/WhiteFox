

Create a model with broadcast to and gather pattern.

class Model(tf.keras.Model):
  def __init__(self):
    super(Model, self).__init__()

  def call(self, t):
    bcast = tf.broadcast_to(t[:,None], [4,4])
    gather1 = tf.gather(bcast, [0,1,2,3])
    gather2 = tf.gather(bcast, [1,2,3,0])
    return gather1, gather2

#Initializing the model
m = Model()

#Inputs to the model
t = tf.constant([0.25, 0.5, 0.4, 0.3])

#Call model
y1, y2 = m(t)