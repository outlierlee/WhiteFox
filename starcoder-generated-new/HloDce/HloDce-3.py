
class Model(tf.keras.Model):

    def __init__(self):
        super(Model, self).__init__()

    def call(self, x):
        # Unused Add operation inside while loop
        while True: 
            tf.add(x, x)
        
        # Used multiply operation outside the while loop
        return tf.multiply(x, x)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x = tf.constant([1.,1.,1.,1.], shape=input_shape)

# Call model
y = m(x)
```

In this example, the model has a `tf.add(x, x)` operation inside a `while` loop that is never executed. Because the `tf.add` operation does not have a side effect (does not modify the state of the computation) and does not have a constrained layout, it is considered dead and will be removed by the `HloDCE` optimization pass. 

The `tf.multiply(x, x)` operation outside of the `while` loop is used in the computations of this model (since it is referenced by the `call` method) and is not considered dead. It will not be removed by the optimization pass.