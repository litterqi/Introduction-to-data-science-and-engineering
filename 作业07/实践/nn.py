import torch.nn as nn
import torch.nn.functional as F
class block(nn.Module):
    def __init__(self,in_channel,outchannel) -> None:
        super().__init__()
        self.cov=nn.Conv2d(in_channel,outchannel,3,padding=1)
        self.BN=nn.BatchNorm2d(outchannel)
        self.pool=nn.MaxPool2d(2,2)
    def forward(self,x):
        x=self.cov(x)
        x=self.BN(x)
        x=F.relu(x)
        x=self.pool(x)
        return x
class VGG(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.cov=nn.Sequential
        (
            block(1,64),
            block(64,128),
            block(128,256),
            block(256,512)
        )
        self.classifier=nn.Sequential
        (
            nn.Linear(512*4*4,1024),
            nn.ReLU(),
            nn.Linear(1024,512),
            nn.ReLU(),
            nn.Linear(512,num_class)
        )    
    def forward(self,x):
        x=self.cov(x)
        x=x.view(-1,512*4*4)
        x=self.classifier(x)
        return x