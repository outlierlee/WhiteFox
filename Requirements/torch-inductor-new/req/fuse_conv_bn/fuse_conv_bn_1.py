The model should contain the following pattern:

1. **Convolution Layer Followed by Batch Normalization Layer**:
   - A convolutional layer (`torch.nn.Conv1d`, `torch.nn.Conv2d`, or `torch.nn.Conv3d`) is immediately followed by a batch normalization layer (`torch.nn.BatchNorm1d`, `torch.nn.BatchNorm2d`, or `torch.nn.BatchNorm3d`).
   - Both layers must be in evaluation mode (`eval()`), meaning they are not in training mode.
   - The batch normalization layer must be tracking running statistics (`track_running_stats=True`).

2. **Constraints on Node Usage**:
   - The output of the convolution layer is used exclusively by the batch normalization layer, meaning it should not be used by any other nodes in the graph.

3. **Batch Normalization Function with Convolution**:
   - Alternatively, the model can use a convolution layer followed by a functional batch normalization (`F.batch_norm`).
   - The batch normalization function must have exactly 8 arguments, and the arguments related to batch normalization parameters (mean, variance, weight, bias) must be constants (i.e., obtained via `get_attr` and used only once).
   - The batch normalization function must not be in training mode, and the epsilon (`eps`) parameter must be a float.

These patterns characterize scenarios where a convolution operation is directly followed by a batch normalization operation, either as a module or a function, and the conditions for fusing these operations are met.