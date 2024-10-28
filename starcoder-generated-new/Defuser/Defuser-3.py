
class M(tf.Module):
  @tf.function(input_signature=[tf.TensorSpec(shape=[1], dtype=tf.float32)], experimental_compile=True)
  def model(self, input):
    t1 = tf.add(input, input)
    t2 = tf.maximum(t1, input)
    return t2

# Additional code to compile the graph and optimize through XLA
concrete_function = m.model.get_concrete_function(tf.TensorSpec(shape=[1], dtype=tf.float32))
graph = concrete_function.graph

jit = tfc.experimental.jit(graph)

jit_graph_def = jit._get_concrete_function().graph.as_graph_def()
```

Please install TensorFlow nightly version (v2.6 or above) for your python environment. The `experimental_compile=True` flag ensures that the model graph is compiled with XLA. If successful, the transformed computations will have fusion instructions and trigger the `Defuser` optimization pass, otherwise, this code will invalidate for normal version of TensorFlow.