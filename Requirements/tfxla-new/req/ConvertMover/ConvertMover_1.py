# Example of increasing precision
x = tf.constant([...], dtype=tf.float16)
y = tf.convert_to_tensor(x, dtype=tf.float32)
z = tf.pad(y, paddings=[[1, 1]], constant_values=0.0)

# Example of decreasing precision
a = tf.constant([...], dtype=tf.float32)
b = tf.convert_to_tensor(a, dtype=tf.float16)
c = tf.reshape(b, new_shape=[...])
