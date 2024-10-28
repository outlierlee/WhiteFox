
class ConvBatchNorm(torch.nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding)
        self.bn = torch.nn.BatchNorm2d(out_channels)

    def forward(self, x):
        
        return self.bn(self.conv(x))

# Initializing the model
model = ConvBatchNorm(in_channels=3, out_channels=5, kernel_size=3, stride=2, padding=1)

# Generating input tensor
x = torch.randn(1, 3, 224, 224)
