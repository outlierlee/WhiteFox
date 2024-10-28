
class Model(tf.keras.Model):

    def __init__(self):
        super(Model, self).__init__()

    def call(self, x):
        i = tf.constant(0)
        result = []
        while_body = lambda i, result: (
            tf.add(i, 1), result + [tf.constant(1)]  # invariant operation
        )
        _, part = tf.while_loop(lambda i, y: tf.less(i, x), while_body, [i, result])
        return part