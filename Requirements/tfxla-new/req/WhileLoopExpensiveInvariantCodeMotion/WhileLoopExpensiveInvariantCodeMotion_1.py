def loop_body(state):
    invariant_tensor = tf.constant([...])  # Expensive invariant operation
    # Use invariant_tensor in some computation
    result = some_computation(state, invariant_tensor)
    return result

initial_state = (tf.zeros(...),)
result = tf.while_loop(cond, loop_body, initial_state)
