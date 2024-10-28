import tensorflow as tf

# Define a simple function with a single operation
def simple_function(x):
    return x * 2  # Single operation

# Use tf.map_fn with the simple function
input_tensor = tf.constant([1, 2, 3, 4])
output_tensor = tf.map_fn(simple_function, input_tensor)
