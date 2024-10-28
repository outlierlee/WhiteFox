
To generate this kind of model, can randomly generate such operations. For example, the below code generates a simple program of two while loop. The first loop increases an integer variable and the second loop decreases it until it reaches zero:

```python
class InvariantLoopOp(tf.raw_ops.While):

    def __init__(self):
        super(InvariantLoopOp, self).__init__()

    def call(self):
        self.x = tf.constant(0, shape=())
        self.i = tf.constant(0, shape=())
        self.cond = lambda: tf.abs(self.i) < tf.constant(10)
        self.body = lambda: self._build_loop_body()
        self.loop = tf.raw_ops.While(self.cond, self.body)
        return self.loop

    @tf.function
    def _build_loop_body(self):
        # Constant+Equal operations in the body make the loop invariant.
        self.y = tf.constant(5)
        self.x = tf.add(self.x, self.y)
        # supports 2 different loop termination operations
        self.i = tf.abs(tf.add(self.i, self.y))
        # if this one is true, output can be hoisted
        self.control_preds = tf.constant(False)
        return (self.x, self.i, self.control_preds)


invariant_loop = InvariantLoopOp()
invariant_loop()

```
The generated model will give the `tf.raw_ops` loop operations, try to run it simple generative loop operations which will automatically satisfied the conditions.