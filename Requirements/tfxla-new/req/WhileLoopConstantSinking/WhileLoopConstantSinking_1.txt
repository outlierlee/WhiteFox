The model should contain the following pattern:

1. **While Loop Structure**: The model must include a `while` loop, which is represented by a `tf.while_loop` construct in TensorFlow. The loop should have a condition and a body function.

2. **Tuple Initialization**: The initial value for the loop variables should be a tuple, which is passed as the first argument to the `tf.while_loop`. This tuple should contain elements that are either constants or broadcasts of constants.

3. **Invariant Elements**: Within the loop body, there should be elements of the tuple that remain invariant (i.e., they do not change across iterations). These invariant elements should be constants or broadcasts of constants.

4. **GetTupleElement (GTE) Usage**: The loop body should use `GetTupleElement` (GTE) operations to access elements of the tuple. At least one of these GTE operations should have more than one user, and not all users should be the root of the loop body.

5. **Condition Function**: The condition function of the `while` loop should also access the same tuple elements using GTE operations. These GTE operations in the condition function should have at least one user.

6. **Broadcast of Constants**: If the model uses broadcasts of constants, the broadcast should originate from a constant value.

The pattern ensures that there are constants or broadcasts of constants in the loop's initial tuple that can be sunk into the loop body and condition, triggering the optimization pass.