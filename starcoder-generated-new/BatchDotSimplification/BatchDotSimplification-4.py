
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.constant([2.,2.,2.,2.,
                      2.,2.,2.,2.,
                      2.,2.,2.,2.,
                      2.,2.,2.,2.], shape=[4,2,3])

    return tf.linalg.batch_matmul(x1, x2, adj_x=True, adj_y=True) 
    

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [3, 3, 4]
x1 = tf.constant([1.,1.,1.,1.,
                  1.,1.,1.,1.,
                  1.,1.,1.,1.], shape=input_shape)

# Call model
y = m(x1)
```
Please generate your valid TensorFlow model that suits both the mentioned requirements. Both reshaping pattern and batch_matmul need to be introduced in the model.