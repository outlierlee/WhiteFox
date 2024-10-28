

Assuming we have a 2-dimensional input tensor with shape [4,8] and four tensors participating in the all_gather operation, all_gather variables will be defined as:

```

class Model(tf.keras.Model):
    
    def __init__(self):
        super(Model, self).__init__()

    def call(self, x1):
        x2 = tf.broadcast_to(x1, [4,4])
        gather_indices = tf.constant([0,0,2,2])
        return tf.all_gather(x2, gather_indices)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4,8]
x1 = tf.constant([[1, 1, 1, 1, 1, 1, 1, 1],\
                  [3, 3, 3, 3, 3, 3, 3, 3],\
                  [4, 4, 4, 4, 4, 4, 4, 4],\
                  [6, 6, 6, 6, 6, 6, 6, 6]], shape=input_shape)

# Call model
y = m(x1)
print(y)
```
This code will create a 4-tensor with 8, 4, 8, 6 dimensions for all_gather operation to be non-uniform along the '1st' dimension.
The model will print a reshaped tensor with 1 before all_gather. Thus, triggering the optimization pass.