import tensorflow as tf

# Assume input_tensor is a tensor with rank > 0
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Non-scalar index tensor with rank 1
index_tensor = tf.constant([1, 0])

# Dynamic slice operation using a non-scalar index
sliced_tensor = tf.raw_ops.DynamicSlice(
    input=input_tensor,
    index=index_tensor,
    size=[1, 3]
)

# Alternatively, a dynamic update slice operation
update_tensor = tf.constant([[9, 9, 9]])
updated_tensor = tf.raw_ops.DynamicUpdateSlice(
    input=input_tensor,
    update=update_tensor,
    index=index_tensor
)
