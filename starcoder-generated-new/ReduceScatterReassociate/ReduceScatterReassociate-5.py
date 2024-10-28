:
class Model(tf.keras.Model):
  
  def __init__(self):
    super(Model, self).__init__()
    self.layernorm = tf.keras.layers.LayerNormalization(axis=None, center=False, scale=False)

  def call(self, x, init_states):
    x = self.layernorm(x)
    
    # First reduce scope
    y1 = self.ops_to_keep_reduce_scatter(x, init_states[0], reduce_kind="SUM", scatter_dim=0, scatter_div=4)
    
    # Second reduce scope
    y2 = self.ops_to_keep_reduce_scatter(x, init_states[1], reduce_kind="SUM", scatter_dim=1, scatter_div=4)
    
    # Apply some operation
    layer_output = tf.reduce_sum([y1,y2], axis=0)
    
    return layer_output
  
  # Method to implement `ops_to_keep_reduce_scatter` optimization for `ReduceScatter`
  def ops_to_keep_reduce_scatter(self, input_tensor, vals, reduce_kind, scatter_dim, scatter_div):
    shards = tf.raw_ops.Shard(input_tensor=input_tensor, num_shards=scatter_div)
    reduce_scatters = tf.raw_ops.ReduceScatter(input_tensor=shards, reduction=reduce_kind, shape=vals.shape, scatter_dims=[scatter_dim], cluster_spec=vals.cluster_spec)
    new_val = tf.raw_ops.UpdateByReduction(input_val=vals, reduction_indicator=[[reduce_kind]], cluster_spec=reduce_scatters.cluster_spec)
    
    return new_val