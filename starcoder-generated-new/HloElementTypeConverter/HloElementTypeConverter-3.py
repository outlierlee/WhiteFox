
class M(tf.Module):
  @tf.function(input_signature=[tf.TensorSpec(shape=(None,), dtype=tf.float32),
                                tf.TensorSpec(shape=(None,), dtype=tf.float32)])
  def add(self, x, y):
    return tf.add(x, y)
  
m = M()
```

After performing the optimization, we can check if the physical types of the computation's instruction results are indeed of type `replace_with_type_`. Unfortunately, TensorFlow XLA does not provide a way to check the actual physical type of the instruction results. This seems to be more out of scope for TensorFlow/XLA's current capability.