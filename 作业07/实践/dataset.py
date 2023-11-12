import matplotlib.pyplot as plt
from torch.utils.data import Dataset,DataLoader
from PIL import Image
class MyDataset(Dataset):
    def __init__(self, txt_path, num_class=20, transforms=None):
        super(MyDataset, self).__init__()
        images = [] 
        labels = [] 
        with open(txt_path, 'r') as f:
            for line in f:
                if int(line.split('/')[-2]) >= num_class:  
                    break
                line = line.strip('\n')
                images.append(line)
                labels.append(int(line.split('/')[-2]))
        self.images = images
        self.labels = labels
        self.transforms = transforms 
    def __getitem__(self, index):
        image = Image.open(self.images[index]).convert('RGB') 
        label = self.labels[index]
        if self.transforms is not None:
            image = self.transforms(image)
        image=image.float().to(dev)
        label=torch.tensor(label).to(dev)
        return image, label
    def __len__(self):
        return len(self.labels)