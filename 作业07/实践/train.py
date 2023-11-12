from torchvision import transforms
trans=transforms.Compose([
                          transforms.PILToTensor(),
                          transforms.Grayscale(1),
                          transforms.Resize((56,56)),
                          transforms.Pad(4,255),
                          transforms.ColorJitter(contrast=(0,255)),
                          ])
train_dataset=MyDataset('train_class_txt.txt',num_class,transforms=trans)
test_dataset=MyDataset('test_class_txt.txt',num_class,transforms=trans)
batch_size=128
train_dl=DataLoader(train_dataset,batch_size=batch_size,shuffle=True)
test_dl=DataLoader(test_dataset,batch_size=2*batch_size)