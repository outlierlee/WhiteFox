
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    self._matchers = {'add': self._add_matcher}

  def call(self, x):
    return tf.add(x, 1) # change x to a new type

  def find_matchers(self, input_tensors):
    #In this case we only consider one added case: add
    return [self._matchers['add'](input_tensors)]

  def apply_transformations(self, match_results):
    #Match results contains a list which has a tuple: (match_tk, operation)
    #The operation includes function name, function parameters etc.
    for match_result in match_results:
      print(f'match result: operation:{match_result[1]}, op_matcher:{match_result[0]}')
      match_result[0].struct_proto().new_form_proto
    return

  def _add_matcher(self, tensor):
    #In this case, we only match add operation, so the input should be an int, and output an int.
    return [('test', tensor[0])]


#Initializing the model
m = Model()

#Inputs to the model
input_shape = [4]
x = tf.constant([4.,5.,6.,7.], shape=input_shape)

#Call model
y = m(x)

#Apply transform
m.apply_transformations(m.find_matchers(x))
```

Note: Both model Pythons codes must use `tf.keras.Model` and only public TensorFlow APIs for the optimization to work. Optimization is the process of re-writing graph to reduce computation and memory, and TensorFlow XLA is designed for this.