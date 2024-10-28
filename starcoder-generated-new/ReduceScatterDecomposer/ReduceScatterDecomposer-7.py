
This is a simplified version of a model that might help to start achieving this optimization:

```python
import tensorflow as tf
from tensorflow.python.framework import dtypes
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import variable_scope
from tensorflow.python.ops.control_flow_ops import create_or_get_global_step

def reshape_and_scatter(input_tensor, do_reshape):
  if do_reshape:
    logits = tf.reshape(input_tensor, [1, -1])
  else:
    logits = input_tensor

  reduced_scatter = tf.xla.experimental.reduce_scatter(logits, ...)

  return reduced_scatter

m = reshape_and_scatter(input_tensor, do_reshape=True)
```

