# Assume eliminate_type_ is float32 and replace_with_type_ is float64
input_tensor = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
result = tf.math.add(input_tensor, input_tensor)  # Arithmetic operation with float32
