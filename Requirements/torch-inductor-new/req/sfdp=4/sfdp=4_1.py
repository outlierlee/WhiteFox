# Compute scaled dot-product attention weights
scaled_scores = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1))
# Optionally add an attention mask
if attn_mask is not None:
    scaled_scores += attn_mask
# Apply softmax to obtain attention weights
attn_weight = torch.softmax(scaled_scores, dim=-1)
# Compute the attention output by multiplying the attention weights with the value tensor
output = attn_weight @ value
