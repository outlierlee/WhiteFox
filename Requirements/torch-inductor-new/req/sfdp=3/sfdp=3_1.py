# Compute scaled dot-product attention
# Step 1: Compute the dot product of the query and the transposed key
attention_scores = torch.matmul(query, key.transpose(-2, -1))

# Step 2: Scale the attention scores by a factor
scaled_attention_scores = attention_scores.mul(scale_factor)

# Step 3: Apply the softmax function to the scaled attention scores
attention_weights = scaled_attention_scores.softmax(dim=-1)

# Step 4: Apply dropout to the attention weights
attention_weights = torch.nn.functional.dropout(attention_weights, p=dropout_p)

# Step 5: Compute the weighted sum of the value vectors
output = attention_weights.matmul(value)
