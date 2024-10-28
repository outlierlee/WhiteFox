

Create a class Model defines a model associating with TensorFlow API that performs a batch dot product operation. Given a lhs tensor, rhs tensor and a contracting dimension, it does the requested mathematical operation followed by reshaping the result to match the original size of the lhs tensor after the operations.

```python
import tensorflow as tf

class Model(tf.keras.Model):
  
  def __init__(self):
    super(Model, self).__init__()

  def call(self, lhs, rhs, contracting_dimension):
    # transpose the rhs tensor to match the lhs tensor
    rhs_transpose = tf.transpose(rhs, perm=list(range(contracting_dimension)) + [0, 2] + list(range(contracting_dimension+1, len(rhs.shape))))
    
    # perform batch matmul
    result = tf.linalg.batch_matmul(lhs, rhs_transpose)
    
    # reshape the result to the original size of the lhs tensor
    result_reshaped = tf.reshape(result, lhs.shape[1:])
    
    return result_reshaped
```

# Usage
Initialize the Model, create two tensors lhs and rhs of shape `[2, 3, 4, 5]` for `lhs` and `[2, 3, 5, 6]` for `rhs`, and set the contracting dimension to `2`, then call the model function to obtain the result.

```python
m = Model()
lhs = tf.random.uniform(shape=[2, 3, 4, 5])
rhs = tf.random.uniform(shape=[2, 3, 5, 6])
contracting_dimension = 2
result = m(lhs, rhs, contracting_dimension)
```

Note: This model uses only functions from TensorFlow's public API and may not cover multiple batches cases, including cumulative product followed by summation, or element-wise operations, etc.