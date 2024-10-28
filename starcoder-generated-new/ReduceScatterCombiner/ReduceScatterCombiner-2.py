

Assuming we have n total bytes of input_tensor data, 

```python
t1 = tf.constant([n // 2] * (n // 4)
t2 = tf.constant([n // 2] * (n // 4)
t3 = tf.constant([n // 2] * (n // 4)
t4 = tf.constant([n // 2] * (n // 4)
t5 = tf.constant([n // 2] * (n // 2)

model = tf.raw_ops.ReduceScatter(input=t1, reduction_op='add')
model = tf.raw_ops.ReduceScatter(input=t2, reduction_op='add')
model = tf.raw_ops.ReduceScatter(input=t3, reduction_op='add')
model = tf.raw_ops.ReduceScatter(input=t4, reduction_op='add')
model = tf.raw_ops.ReduceScatter(input=t5, reduction_op='add')
```

Please note, generating such a model involves the use of raw ops, which are candidates for deletion or re-evaluated before the onnx converter would convert this to a xla-flop compatible format.