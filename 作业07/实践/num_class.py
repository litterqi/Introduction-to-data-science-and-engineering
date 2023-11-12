import os
num_class=100 
def class_txt(root,out_path,num_class=20):
    dirs=os.listdir(root)
    if not num_class:
        num_class=len(dirs)
    if not os.path.exists(out_path):
        f=open(out_path,'w')
        f.close()
    with open(out_path,'r+') as f:
        try:
            end = int(f.readlines()[-1].split('/')[-2]) + 1
        except:
            end = 0
        if end < num_class - 1:
            dirs.sort()
            dirs = dirs[end:num_class]
            for dir in dirs:
                files = os.listdir(os.path.join(root, dir))
                # print(os.path.join(root,dir)+'/'+files[0])
                for file in files:
                    f.write(os.path.join(root, dir)+'/'+file + '\n')

train_path='./../train/'
test_path='./../test/'

class_txt(train_path,'train_class_txt.txt',num_class=num_class)
class_txt(test_path,'test_class_txt.txt',num_class=num_class)