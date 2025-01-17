# Compute scaled dot-product attention weights
scaled_scores = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1))

# Add an attention mask to the scaled scores
masked_scores = scaled_scores + attn_mask

# Apply softmax to obtain attention weights
attn_weight = torch.softmax(masked_scores, dim=-1)

# Apply dropout to the attention weights
attn_weight = torch.dropout(attn_weight, dropout_p, True)

# Compute the attention output by multiplying the attention weights with the value tensor
output = attn_weight @ value
