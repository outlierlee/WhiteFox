def model(input_tensor):
    # Some initial computations
    x = tf.add(input_tensor, 1)
    
    # Dead computation
    y = tf.multiply(x, 0)  # This result is never used
    
    # Removable while loop
    def cond(x):
        return tf.less(x, 10)
    
    def body(x):
        return tf.add(x, 1)
    
    z = tf.while_loop(cond, body, [x])  # This loop does not affect the final output
    
    # Final output
    return tf.add(x, 2)
