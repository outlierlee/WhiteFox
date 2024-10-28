
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    return tf.reshape(x1, [0])

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [0]
x1 = tf.constant([1], shape=input_shape)

# Call model
y = m(x1)

The above created models will trigger `ZeroSizedHloElimination` in TensorFlow XLA on the runner side. As of now, wrapping these models in run_hlo_module will not trigger optimization pass through XLA API. You need to run these models in a TensorFlow session (by calling session.run with the above models) or run tensorflow XLA flags directly on the python command-line. 

```
--config=hlo.remove_zero_sized_dims=true
```
To receive the triggers through XLA API will likely need add-ons to the XLA compiler or to reengineer XLA to take advantage of such triggers, or TensorFlow will need to add them to its native set of run-time optimization passes opted-in to be triggered at execution time.