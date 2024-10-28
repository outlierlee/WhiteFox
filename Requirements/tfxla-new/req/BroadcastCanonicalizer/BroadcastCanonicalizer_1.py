   import tensorflow as tf

   # Assume `input_tensor` is a tensor with shape [a, b, c]
   input_tensor = tf.constant(...)

   # Broadcasting `input_tensor` to a higher-dimensional shape with unsorted dimensions
   # For example, broadcasting to shape [1, a, 1, b, c] with broadcast dimensions [1, 3, 4]
   broadcasted_tensor = tf.broadcast_to(input_tensor, [1, a, 1, b, c])
