# Compute the dot product between the query and the transposed key
scores = torch.matmul(query, key.transpose(-2, -1))

# Scale the scores by dividing with a scaling factor (often the square root of the dimension of the key)
scaled_scores = scores.div(inv_scale)

# Apply the softmax function to the scaled scores along the last dimension to obtain attention weights
attention_weights = scaled_scores.softmax(dim=-1)

# Compute the weighted sum of the value vectors using the attention weights
output = attention_weights.matmul(value)
