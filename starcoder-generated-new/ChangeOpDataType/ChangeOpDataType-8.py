

class CustomOp(tf.raw_ops.Something):
  def __init__(self, conversion, num_tensors_required):
    super(CustomOp, self).__init__(*args, **kwargs)
    self._conversion = conversion
    self._num_tensors_required = num_tensors_required

  def op(self, *input_tensors):
    result = self._gen_call_op_helper(
        sys.stderr, 'Op', input_tensors,
        self._conversion, self._num_tensors_required)
    return result


class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = CustomOp(to_type_map_[x1.dtype], num_tensors_required = 1)
    return x2(x1)


# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([123456, 123456, 123456, 123456], shape=input_shape, dtype=tf.int32)


# Call model
y = m(x1)

```
The `CustomOp` described above is a placeholder. Please replace `CustomOp` with the real custom op you want. 

Pay attention: Be careful about input arguments of op if the only awareness of TensorFlow cannot guide you how your custom op should be written. Consult TensorFlow (Python) APIs and documentation, or ask for TensorFlow Community if you need help.