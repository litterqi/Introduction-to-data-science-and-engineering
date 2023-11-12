epochs=50
for epoch in range(epochs):
    model.train()
    for xb,yb in train_dl:
        pred=model(xb).to(dev)
        loss=loss_func(pred,yb)
        loss.backward()
        opt.step()
        opt.zero_grad()
    model.eval()
    with torch.no_grad():
        test_loss=sum(loss_func(model(xb),yb) for xb,yb in test_dl)
    print(epoch,test_loss/len(test_dl))