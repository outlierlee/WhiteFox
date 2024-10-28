
Consider the following model:

```python
def dead_computation_model(x):
    y = tf.add(x, x)  # This computation is not used anywhere
    return tf.multiply(x, y)  # y is also not used elsewhere, but the computation to which y is associated with is used. Hence, it has dependence on y and will not be removed by DCE.
```

This model has a dead part of computation -- `y = tf.add(x, x)` since it appears after the first computation `tf.multiply(x, y)` thus, it will not be changed by the Dead Code Elimination optimization pass, demonstrating the above dead code removal requirements.