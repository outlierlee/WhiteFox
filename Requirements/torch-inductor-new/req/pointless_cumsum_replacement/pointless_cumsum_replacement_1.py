# Create a tensor filled with ones
t1 = torch.full(size=[Arg(), Arg()], fill_value=1, dtype=Ignored(), layout=Ignored(), device=device, pin_memory=False)

# Convert the element type of the tensor to a specified dtype
t2 = prims.convert_element_type(t1, dtype=dtype)

# Compute the cumulative sum of the tensor along dimension 1
t3 = torch.cumsum(t2, dim=1)
