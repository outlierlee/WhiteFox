
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, loop_cond_val, loop_body_val):
    # Case where loop_body_val is invariant across loop iterations
    loop_cond_val = tf.constant(0)
    loop_body_val = tf.constant(5)

    def condition(i, val):
      return i < loop_cond_val

    def body(i, val):
      return i + 1, val * loop_body_val # loop_body_val is invariant across iterations

    _, result_with_invariant_val = tf.while_loop(condition, body, [0, loop_body_val])

    # Case where loop_body_val is not invariant across loop iterations
    loop_cond_val = tf.constant(0)
    loop_body_val = tf.constant([5,10])

    def condition(i, val):
      return i < loop_cond_val

    def body(i, val):
      return i + 1, val * tf.constant([3,2]) # val changes across iterations

    _, result_with_non_invariant_val = tf.while_loop(condition, body, [0, loop_body_val])

    return result_with_invariant_val, result_with_non_invariant_val

# Initializing the model
m = Model()

# Inputs to the model
loop_cond_val = tf.constant(0)
loop_body_val = tf.constant(5)

# Call model
result_with_invariant_val, result_with_non_invariant_val = m(loop_cond_val, loop_body_val)