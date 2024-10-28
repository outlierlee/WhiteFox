t1 = input_tensor_A.permute(...) # Permute the first input tensor
t2 = input_tensor_B.permute(...) # Permute the second input tensor
t3 = torch.matmul(t1, t2) # Apply matrix multiplication to the permuted tensors.
t1 = input_tensor_A.permute(...) # Permute the first input tensor
t2 = torch.matmul(t1, input_tensor_B) # Apply matrix multiplication with the permuted first tensor.
t1 = input_tensor_B.permute(...) # Permute the second input tensor
t2 = torch.matmul(input_tensor_A, t1) # Apply matrix multiplication with the permuted second tensor.
