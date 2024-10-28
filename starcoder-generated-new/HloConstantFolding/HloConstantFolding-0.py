
class Model(tf.Module):

  def __init__(self):
    super(Model, self).__init__()
    self.constant_1 = tf.constant([4.], shape=[1])
    self.constant_2 = tf.constant([5.], shape=[1])
    self.constant_3 = tf.constant([6.], shape=[1])
    self.constant_4 = tf.constant([7.], shape=[1])

  @tf.function
  def forward(self):
    return self.constant_1 + self.constant_2 + self.constant_3 + self.constant_4

# Initializing the model
m = Model()

print(m.forward())