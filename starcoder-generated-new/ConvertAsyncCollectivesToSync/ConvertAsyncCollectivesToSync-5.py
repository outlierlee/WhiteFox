
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    async_start = tf.xla.experimental.start_async_outbound_data_transfer(x1, 0)
    async_done = tf.xla.experimental.done_async_outbound_data_transfer(async_start)
    return async_done

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
```

Remember that the output `async_done` is then used as an input to another layer in the model.


Note: The XLA debugger will not work for these models as the tests are generated automatically and cannot be manually debugged. They are likely to give the incorrect result, but it should nonetheless work as intended.


Please note - this code will not run correctly unless you explicitly aim for XLA compilation compatible with Tensorflow 2.6.0rc0. At time of writing, JAX is incompatible with TensorFlow XLA on a regular build. As such, using the async collective handle as a constant here or as an input to another layer in the model will fail.