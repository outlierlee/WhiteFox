
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
      
    @staticmethod
    def is_valid_splitwithsizes_cat(model):
        split_ops = [op for op in model.graph.get_operations() if op.type == "Split"]
        cat_ops = [op for op in model.graph.get_operations() if op.type == "Concat"]
    
        if len(split_ops) != 1 or len(cat_ops) != 1: # Check 'Split' and 'Concat' operation is only once
            return False
        
        split_dim = [value for value in split_ops[0].inputs[1].values()[0]][0] 
        cat_dim = [value for value in cat_ops[0].inputs[1].values()[0]][0] 
        
        if split_dim != cat_dim: # The 'Split' and 'Concat' operation's dim should be same
            return False
        
        split_outputs = [output.name for output in model.graph.find(split_ops[0], model.outputs)]
        cat_outputs = [output.name for output in model.graph.find(cat_ops[0], model.outputs)]
        
        if split_outputs != cat_outputs: # All split tensors should be used in concatenation
            return False
        
        return True # The model is valid

    def forward(self, x):
        x1 = x.clone()
        split_sizes = [3,3,4] 
        split_x1 = torch.split(x1, split_sizes, dim=1)
        return torch.cat(split_x1, dim=1) # Concatenate the split tensors along the dimension 1

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 10, 64, 64)
