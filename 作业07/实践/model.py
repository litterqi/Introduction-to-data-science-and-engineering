model=VGG().to(dev)
opt=torch.optim.SGD(model.parameters(),lr=0.01)
loss_func=F.cross_entropy