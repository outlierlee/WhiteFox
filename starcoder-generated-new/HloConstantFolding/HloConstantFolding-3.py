
class M(tf.Module):
  @tf.function(input_signature=[tf.TensorSpec(shape=(1,), dtype=tf.float32)])
  def func(self, x):
    return tf.numpy_function(func, [x], Tout=tf.int32)

# Create instance of the module
m = M()

# Create a function that determines if the Hlo part has to be recompiled
def run():
  llvm_context = xla.backend.DataTypeDT_INT32
  hlo_module = tf.function(func, autograph=False).get_concrete_function(1)._concrete_function._unwrapped_python_func._wrapped_function.graph.__self__._signature[0]._xla
  return tf.config.optimizer.experimental_optimize(llvm_context, hlo_module)

# This will return True because the XLA compilation graph contains the HloConstantFolding optimization which is designed to optimize operations where one operand is a constant, and all other operands are either constants or broadcasts of constants.
print(run())