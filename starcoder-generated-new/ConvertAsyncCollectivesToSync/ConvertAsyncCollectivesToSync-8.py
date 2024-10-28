

Create a custom layer defines to represent associative operation in the model. 

```python
class AssocOpLayer(tf.keras.layers.Layer):
  def __init__(self):
    super(AssocOpLayer, self).__init__()

  def call(self, x):
    async_start = tf.xla.experimental.start_async_outbound_data_transfer(payload=None, transfer_id=None,
                                                                          shape=None, token=None)
    async_done = tf.xla.experimental.done_async_outbound_data_transfer(async_start)
    return async_start, async_done
```

Initialize the custom layer and use it in a model.

```python
layer = AssocOpLayer()
model = tf.keras.models.Sequential([
    tf.keras.layers.InputLayer(input_shape=[4]),
    layer
])
```