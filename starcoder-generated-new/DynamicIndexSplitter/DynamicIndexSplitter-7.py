
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    indices = tf.constant([1, 0])
    return tf.dynamic_update_slice(x1, tf.constant([10., 10.]), indices)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)


Please generate one valid TensorFlow model that satisfies requirements below.
You should only use public TensorFlow APIs. The model can be used as the input to trigger the optimization pass `TransposePermutation` in TensorFlow XLA.

# Description
The model should contain the following pattern:
```
t1 = tf.transpose(input_tensor, perm=[...])
t2 = tf.transpose(t1, perm=[...])
```
or
```
t1 = tf.transpose(input_tensor, perm=[...])
t2 = tf.transpose(t1, perm=[...])
t3 = tf.transpose(t2, perm=[...])
```
The pattern describes that there are n transpose operators, where n can be 2 or 3. The output shape of the first `transpose` is permuted based on perm=[...], and its second output shape is permuted based on perm=[...]. The second `transpose` has its first input from the first `transpose` and permutes again based on perm=[...]. If n=3, a third `transpose` is added with its first input from the second `transpose`.

The optimization pass `TransposePermutation` is triggered when the output shape of the transpose operation is not affected by its input shape. In these cases, the transpose operation can be skipped, reducing the complexity of the model.

# Model
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    t1 = tf.transpose(x, perm=[2,0,1])
    t2 = tf.transpose(t1, perm=[2,0,1])
    return t2

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2,2,2]
x = tf.constant([[[1,2],[3,4]],
                 [[5,6],[7,8]],
                 [[9,10],[11,12]]], 
                 shape=input_shape)

# Call model
y = m(x);