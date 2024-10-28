def body_fn(loop_var):
    # Define the loop body operations
    return loop_var - 1

def cond_fn(loop_var):
    # Define the loop condition
    return loop_var > 0

initial_value = tf.constant(10)
result = tf.while_loop(cond_fn, body_fn, [initial_value])
