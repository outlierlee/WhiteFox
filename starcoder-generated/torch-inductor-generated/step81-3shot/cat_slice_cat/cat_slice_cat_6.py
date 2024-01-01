
class Model(torch.nn.Module):
    def forward(self, x1, x2):
        v1 = torch.cat((x1, x2), dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:x2.size()[1]]
        v4 = torch.cat([v1, v3], dim=1)
        return v4

# Initializing the model
m = Model()

# Input to the model
x1 = torch.randn(1, 868, 868, 868)
x2 = torch.randn(1, 999, 868, 868)