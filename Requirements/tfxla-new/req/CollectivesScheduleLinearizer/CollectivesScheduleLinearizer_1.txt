The model should contain the following pattern:

1. **Collective Operations**: The model must include multiple collective operations, such as `AllReduce`, `AllGather`, `CollectivePermute`, or their asynchronous variants (`AllReduceStart`, `AllGatherStart`, `CollectivePermuteStart`, etc.).

2. **Independence**: These collective operations should be independent of each other in terms of execution order. This means that there are no existing control dependencies or data dependencies that enforce a specific order between them.

3. **Asynchronous Variants**: If asynchronous variants are used, the model should ensure that each `AsyncStart` operation has a corresponding `AsyncDone` operation, and these pairs are independent of other collective operations.

4. **Non-fusion Computations**: The collective operations should be part of non-fusion computations within the model, as the optimization pass iterates over non-fusion computations.

5. **Execution Threads**: The model should be executed in a context where the specified execution threads are considered, as the optimization pass takes execution threads into account.

The presence of these characteristics in the model will trigger the `CollectivesScheduleLinearizer` optimization pass, leading to the addition of control dependencies between independent collective operations to enforce a specific execution order.