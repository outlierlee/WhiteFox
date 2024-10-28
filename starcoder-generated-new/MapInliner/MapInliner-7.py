

```python
class Model(tf.keras.Model):

    def __init__(self):
        super(Model, self).__init__()

    @tf.function
    def call(self, x):
        return tf.map_fn(f=lambda x: x**3, elems=x)
        
# Initializing the model
m = Model()

# Inputs to the model
input_shape = [10]
x = tf.constant([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0], shape=input_shape)

# Call model
y = m(x)
```

# The task
Generate the required input for a TensorFlow model to trigger the MapInliner optimization pass in TensorFlow XLA. The model should implement a `map_fn` operation where all inputs to the function are parameters. 

Prepare the TensorFlow model and make sure that your TensorFlow model can be used for triggering the `MapInliner` optimization pass in TensorFlow XLA. 

You should only use public TensorFlow APIs. Please restrict the use of built-in functions where possible.