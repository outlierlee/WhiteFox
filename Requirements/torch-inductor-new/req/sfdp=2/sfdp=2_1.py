# Compute the dot product between the query and the transposed key
attention_scores = torch.matmul(query, key.transpose(-2, -1))

# Scale the attention scores by dividing with a scaling factor
scaled_attention_scores = attention_scores.div(inv_scale_factor)

# Apply the softmax function to the scaled attention scores along the last dimension
attention_weights = scaled_attention_scores.softmax(dim=-1)

# Apply dropout to the attention weights
attention_weights = torch.nn.functional.dropout(attention_weights, p=dropout_p)

# Compute the weighted sum of the value vectors using the attention weights
output = attention_weights.matmul(value)
