   input_tensor = ...
   transposed_input = tf.transpose(input_tensor, perm=[...])
   conv_result = tf.nn.conv2d(transposed_input, filter, ...)
   input_tensor_a = ...
   input_tensor_b = ...
   transposed_a = tf.transpose(input_tensor_a, perm=[...])
   transposed_b = tf.transpose(input_tensor_b, perm=[...])
   dot_result = tf.linalg.matmul(transposed_a, transposed_b)
