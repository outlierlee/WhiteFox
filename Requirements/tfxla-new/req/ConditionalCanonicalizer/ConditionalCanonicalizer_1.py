import tensorflow as tf

def true_fn():
    return tf.constant(1)  # Non-tuple output

def false_fn():
    return tf.constant(0)  # Non-tuple output

# Conditional operation with non-tuple outputs
result = tf.cond(tf.constant(True), true_fn, false_fn)
