
class M(tf.Module):
  @tf.function(input_signature=[tf.TensorSpec(shape=(1,), dtype=tf.float32)])
  def __call__(self, x1):
    x2 = tf.cast(x1, tf.bfloat16)
    return tf.cast(x2, tf.float32)

# Set the concrete function to the experimental property, so it will be
# picked up by the XLA-TF converter and passed to the 'opt_passes' argument.
tf.function(experimental=True)(M)
```

model = tf.Module()
input_shape = [1]
x1 = tf.constant([1.], dtype=tf.float32, shape=input_shape)
y = model(x1)