
class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv0 = nn.Conv2d(1,3,28,1)
        self.bn0 = nn.BatchNorm2d(3, affine=False)
        self.conv1 = nn.Conv2d(3,32,1,1)
        self.conv2 = nn.Conv2d(3,32,3,1)
        self.conv3 = nn.Conv2d(32,32,1,1)
        self.bn1 = nn.BatchNorm2d(32, affine=False)
        self.conv4 = nn.Conv2d(32,32,5,1)
        self.conv5 = nn.Conv2d(32, 32, 1, 1)
        self.bn2 = nn.BatchNorm2d(32, affine=True)
        self.relu = nn.ReLU(inplace=True)
        self.bn3 = nn.BatchNorm2d(32, affine=False)
        self.conv6 = nn.Conv2d(32, 32, 3, 1)
        self.conv7 = nn.Conv2d(32,32,1,1)
        self.bn4 = nn.BatchNorm2d(32, affine=False)
        self.conv8 = nn.Conv2d(32,32,3,1)
        self.conv9 = nn.Conv2d(32,32,1,1)
        self.bn5 = nn.BatchNorm2d(32, affine=True)
        self.relu1 = nn.ReLU(inplace=True)
        self.bn6 = nn.BatchNorm2d(32, affine=False)
        self.conv10 = nn.Conv2d(32,32,3,1)
        self.conv11 = nn.Conv2d(32,32,1,1)
        self.bn7 = nn.BatchNorm2d(32, affine=False)
        self.conv12 = nn.Conv2d(32,32,3,1)
        self.conv13 = nn.Conv2d(32,10,1,1)
    def forward(self, x0):
        x1 = self.conv0(x0)
        x1 = self.bn0(x1)
        x1 = self.conv1(x1)
        x2 = self.conv2(x1)
        x3 = self.conv3(x2)
        x3 = self.bn1(x3)
        x4 = self.conv4(x3)
        x5 = self.conv5(x4)
        x5 = self.bn2(x5)
        x5 = self.conv6(x5)
        x6 = self.conv7(x5)
        x6 = self.bn3(x6)
        x7 = self.conv8(x6)
        x8 = self.conv9(x7)
        x8 = self.bn4(x8)
        x9 = self.conv10(x8)
        x10 = self.conv11(x9)
        x10 = self.bn5(x10)
        x11 = self.conv12(x10)
        x12 = self.conv13(x11)
        return (x12, x12)
# Inputs to the model
x0 = torch.randn(10, 1, 28, 28)