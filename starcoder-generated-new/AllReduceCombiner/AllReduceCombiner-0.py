
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2, x3, x4):
    t1 = tf.reduce_sum(x1)
    t2 = tf.reduce_sum(x2)
    t3 = tf.reduce_sum(x3)
    t4 = tf.reduce_sum(x4)
    
    all_reduce1 = tf.distribute.AllReduce(tf.distribute.ReduceOp.SUM, [t1, t2])
    all_reduce2 = tf.distribute.AllReduce(tf.distribute.ReduceOp.SUM, [t3, t4])

    all_reduce3 = tf.distribute.AllReduce(tf.distribute.ReduceOp.SUM, [all_reduce1.values, all_reduce2.values])
  
    return all_reduce3.values

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([1., 2., 3., 4.], shape=input_shape)
x2 = tf.constant([5., 6., 7., 8.], shape=input_shape)
x3 = tf.constant([1., 2., 3., 4.], shape=input_shape)
x4 = tf.constant([5., 6., 7., 8.], shape=input_shape)

# Call model
y = m(x1, x2, x3, x4)
```

# Instructions
Please don't fill up the Model with any real-world dependent computations. TensorFlow XLA avoids applying this pass to models that contain dynamic behaviors. This model is for testing purposes only.