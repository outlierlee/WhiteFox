
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(0.1)
        self.bn1 = torch.nn.BatchNorm2d(3)
        self.avgpool = torch.nn.AvgPool2d(4)
        self.bn2 = torch.nn.BatchNorm2d(8)
        self.linear = torch.nn.Linear(8, 8)
        self.relu = torch.nn.ReLU()
        self.conv1 = torch.nn.Conv2d(3, 8, 4, stride=4)
        self.conv2 = torch.nn.Conv2d(8, 8, 4, stride=4)
        self.conv3 = torch.nn.Conv2d(8, 16, 4, stride=4)
        self.conv4 = torch.nn.Conv2d(16, 16, 4, stride=4)
        self.mp1 = torch.nn.MaxPool2d(4, stride=4)
    def forward(self, x):
        v1 = self.bn1(x)
        v2 = v1.clone()
        v3 = self.bn2(v1)
        v4 = self.conv1(v3)
        v5 = self.bn2(v4)
        v6 = self.conv2(v5)
        v7 = self.bn2(v6)
        v8 = v7.clone()
        v9 = v7.clone()
        v10 = self.relu(v8)
        v11 = self.conv3(v10)
        v12 = self.relu(v11)
        v13 = self.conv4(v11)
        v13 = self.dropout(v12)
        v14 = v12.clone()
        v15 = self.mp1(v13)
        return v15
# Inputs to the model
x = torch.randn(1, 3, 256, 256)