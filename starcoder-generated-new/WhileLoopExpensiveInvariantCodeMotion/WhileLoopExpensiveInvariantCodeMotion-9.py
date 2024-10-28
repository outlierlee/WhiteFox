

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.constant([1, 2, 3])
    count = 0
    i = 0

    def condition(i):
      return tf.less(i, 10000)

    def body(i): 
      nonlocal x2
      nonlocal count
      x2 = tf.add(x2, x2)  # invariant instruction
      count += 1
      return i + 1, x2

    while_body = body
    result = tf.while_loop(condition, while_body, [i])
    return result

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [3]
x1 = tf.constant([1, 1, 1], shape=input_shape)

# Call model
y = m(x1)
print(y)